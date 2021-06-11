# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.azclierror import DeploymentError, ResourceNotFoundError
from azure.core.exceptions import HttpResponseError
from .._client_factory import (
    k8s_config_sourcecontrol_client,
    k8s_config_extension_client
)
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


class FluxConfigurationProvider:
    def __init__(self, cmd, client, resource_group_name, cluster_name, cluster_type, name=None):
        self.extension_provider = ExtensionProvider(cmd, client, resource_group_name, cluster_name, cluster_type)
        self.cmd = cmd
        self.client = client
        self.resource_group_name = resource_group_name
        self.cluster_name = cluster_name
        self.cluster_type = cluster_type
        self.name = name
        self.cluster_rp = get_cluster_rp(cluster_type)
        

    def show(self):
        """Get an existing Kubernetes Source Control Configuration.

        """
        # Determine ClusterRP
        try:
            config = self.client.get(self.resource_group_name, self.cluster_rp, self.cluster_type, self.cluster_name, self.name)
            return config
        except HttpResponseError as ex:
            # Customize the error message for resources not found
            if ex.response.status_code == 404:
                # If Cluster not found
                if ex.message.__contains__("(ResourceNotFound)"):
                    message = ex.message
                    recommendation = 'Verify that the --cluster-type is correct and the Resource ' \
                                    '{0}/{1}/{2} exists'.format(self.cluster_rp, self.cluster_type, self.cluster_name)
                # If Configuration not found
                elif ex.message.__contains__("Operation returned an invalid status code 'Not Found'"):
                    message = '(ConfigurationNotFound) The Resource {0}/{1}/{2}/Microsoft.KubernetesConfiguration/' \
                            'fluxConfigurations/{3} could not be found!'.format(self.cluster_rp, self.cluster_type,
                                                                                self.cluster_name, self.name)
                    recommendation = 'Verify that the Resource {0}/{1}/{2}/Microsoft.KubernetesConfiguration' \
                                    '/fluxConfigurations/{3} exists'.format(self.cluster_rp, self.cluster_type,
                                                                            self.cluster_name, self.name)
                else:
                    message = ex.message
                    recommendation = ''
                raise ResourceNotFoundError(message, recommendation) from ex


    # pylint: disable=too-many-locals
    def create(self, url=None, scope='cluster', namespace='default', kind=consts.GIT, timeout=None, sync_interval=None,
               branch=None, tag=None, semver=None, commit=None, auth_ref_override=None, ssh_private_key=None,
               ssh_private_key_file=None, https_user=None, https_key=None, known_hosts=None,
               known_hosts_file=None, kustomization=None):

        # Pre-Validation
        validate_repository_ref(branch, tag, semver, commit)
        validate_duration("--timeout", timeout)
        validate_duration("--sync-interval", sync_interval)

        if kustomization:
            validate_kustomization_list(kustomization)

        # Validate if we are able to install the flux configuration
        scc_client = k8s_config_sourcecontrol_client(self.cmd.cli_ctx)
        configs = scc_client.list(self.resource_group_name, self.cluster_rp, self.cluster_type, self.cluster_name)
        # configs is an iterable, no len() so we have to iterate to check for configs
        for _ in configs:
            raise DeploymentError(
                consts.SCC_EXISTS_ON_CLUSTER_ERROR,
                consts.SCC_EXISTS_ON_CLUSTER_HELP)

        # Validate if the extension is installed, if not, install it
        extension_client = k8s_config_extension_client(self.cmd.cli_ctx)
        extensions = extension_client.list(self.resource_group_name, self.cluster_rp, self.cluster_type, self.cluster_name)
        found_flux_extension = False
        for extension in extensions:
            if extension.extension_type.lower() == consts.FLUX_EXTENSION_TYPE:
                found_flux_extension = True
                break
        if not found_flux_extension:
            self.extension_provider.create(self.cmd, self.client, self.resource_group_name, self.cluster_name, self.name, self.cluster_type,
                                           consts.FLUX_EXTENSION_TYPE, "cluster")

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

        return self.client.begin_create_or_update(self.resource_group_name, self.cluster_rp,
                                                  self.cluster_type, self.cluster_name, self.name, flux_configuration)


    def delete(self, client, resource_group_name, cluster_name, cluster_type, name):
        cluster_rp = get_cluster_rp(cluster_type)
        return client.begin_delete(resource_group_name, cluster_rp, cluster_type, cluster_name, name)