# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.azclierror import DeploymentError, ResourceNotFoundError
from azure.core.exceptions import HttpResponseError
from knack.log import get_logger

from .._client_factory import k8s_config_fluxconfig_client
from ..utils import get_cluster_rp, get_data_from_key_or_file, get_protected_settings
from ..validators import (
    validate_cc_registration,
    validate_known_hosts,
    validate_repository_ref,
    validate_duration,
    validate_git_repository,
    validate_kustomization_list,
    validate_private_key,
    validate_url_with_params
)
from .. import consts
from ..vendored_sdks.v2021_06_01_preview.models import (
    FluxConfiguration,
    GitRepositoryDefinition,
    RepositoryRefDefinition,
)
from .ExtensionProvider import ExtensionProvider
from .SourceControlConfigurationProvider import SourceControlConfigurationProvider

logger = get_logger(__name__)

class FluxConfigurationProvider:
    def __init__(self, cmd):
        self.extension_provider = ExtensionProvider(cmd)
        self.source_control_configuration_provider = SourceControlConfigurationProvider(cmd)
        self.cmd = cmd
        self.client = k8s_config_fluxconfig_client(cmd.cli_ctx)
        

    def show(self, resource_group_name, cluster_type, cluster_name, name):
        """Get an existing Kubernetes Source Control Configuration.

        """
        # Determine ClusterRP
        cluster_rp = get_cluster_rp(cluster_type)
        try:
            config = self.client.get(resource_group_name, cluster_rp, cluster_type, cluster_name, name)
            return config
        except HttpResponseError as ex:
            # Customize the error message for resources not found
            if ex.response.status_code == 404:
                # If Cluster not found
                if ex.message.__contains__("(ResourceNotFound)"):
                    message = ex.message
                    recommendation = 'Verify that the --cluster-type is correct and the Resource ' \
                                    '{0}/{1}/{2} exists'.format(cluster_rp, cluster_type, cluster_name)
                # If Configuration not found
                elif ex.message.__contains__("Operation returned an invalid status code 'Not Found'"):
                    message = '(FluxConfigurationNotFound) The Resource {0}/{1}/{2}/Microsoft.KubernetesConfiguration/' \
                            'fluxConfigurations/{3} could not be found!'.format(cluster_rp, cluster_type,
                                                                                cluster_name, name)
                    recommendation = 'Verify that the Resource {0}/{1}/{2}/Microsoft.KubernetesConfiguration' \
                                    '/fluxConfigurations/{3} exists'.format(cluster_rp, cluster_type,
                                                                            cluster_name, name)
                else:
                    message = ex.message
                    recommendation = ''
                raise ResourceNotFoundError(message, recommendation) from ex


    # pylint: disable=too-many-locals
    def create(self, resource_group_name, cluster_type, cluster_name, name, url=None, scope='cluster', namespace='default',
               kind=consts.GIT, timeout=None, sync_interval=None, branch=None, tag=None, semver=None, commit=None, auth_ref_override=None,
               ssh_private_key=None, ssh_private_key_file=None, https_user=None, https_key=None, known_hosts=None,
               known_hosts_file=None, kustomization=None):
        # Determine the cluster RP
        cluster_rp = get_cluster_rp(cluster_type)

        # Pre-Validation
        validate_repository_ref(branch, tag, semver, commit)
        validate_duration("--timeout", timeout)
        validate_duration("--sync-interval", sync_interval)

        if kustomization:
            validate_kustomization_list(kustomization)

        # Validate if we are able to install the flux configuration
        configs = self.source_control_configuration_provider.list(resource_group_name, cluster_type, cluster_name)
        # configs is an iterable, no len() so we have to iterate to check for configs
        for _ in configs:
            raise DeploymentError(
                consts.SCC_EXISTS_ON_CLUSTER_ERROR,
                consts.SCC_EXISTS_ON_CLUSTER_HELP)

        # Validate if the extension is installed, if not, install it        
        extensions = self.extension_provider.list(resource_group_name, cluster_type, cluster_name)
        found_flux_extension = False
        for extension in extensions:
            if extension.extension_type.lower() == consts.FLUX_EXTENSION_TYPE:
                found_flux_extension = True
                break
        if not found_flux_extension:
            logger.warning("'Micrsoft.Flux' extension not found on the cluster, installing it now. This may take a minute...")
            self.extension_provider.create(resource_group_name, cluster_type, cluster_name, "flux", consts.FLUX_EXTENSION_TYPE, release_train="preview")

        # Get the protected settings and validate the private key value
        protected_settings = get_protected_settings(
            ssh_private_key, ssh_private_key_file, https_user, https_key
        )
        if consts.SSH_PRIVATE_KEY_KEY in protected_settings:
            validate_private_key(protected_settings['sshPrivateKey'])

        # Get the known hosts data and validate it
        knownhost_data = get_data_from_key_or_file(known_hosts, known_hosts_file)
        if knownhost_data:
            validate_known_hosts(knownhost_data)

        # Validate registration with the RP endpoint
        validate_cc_registration(self.cmd)

        git_repository = GitRepositoryDefinition()
        dp_source_kind = consts.GIT_REPOSITORY

        if kind == consts.GIT:
            validate_git_repository(url)
            validate_url_with_params(url, ssh_private_key, ssh_private_key_file,
                                    known_hosts, known_hosts_file, https_user, https_key)
            repository_ref = RepositoryRefDefinition(
                branch=branch,
                tag=tag,
                semver=semver,
                commit=commit
            )
            git_repository = GitRepositoryDefinition(
                url=url,
                timeout=timeout,
                sync_interval=sync_interval,
                repository_ref=repository_ref,
                ssh_known_hosts=knownhost_data,
                https_user=https_user,
                auth_ref_override=auth_ref_override
            )

        flux_configuration = FluxConfiguration(
            scope=scope,
            namespace=namespace,
            source_kind=dp_source_kind,
            timeout=timeout,
            sync_interval=sync_interval,
            git_repository=git_repository,
            kustomizations=kustomization
        )

        return self.client.begin_create_or_update(resource_group_name, cluster_rp,
                                                  cluster_type, cluster_name, name, flux_configuration)


    def delete(self, client, resource_group_name, cluster_type, cluster_name, name):
        cluster_rp = get_cluster_rp(cluster_type)
        return client.begin_delete(resource_group_name, cluster_rp, cluster_type, cluster_name, name)