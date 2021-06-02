# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.azclierror import ResourceNotFoundError
from azure.core.exceptions import HttpResponseError
from .utils import get_cluster_type, get_data_from_key_or_file, get_protected_settings
from .validators import (
    validate_cc_registration,
    validate_known_hosts,
    validate_repository_ref,
    validate_duration,
    validate_git_repository,
    validate_kustomization_list,
    validate_private_key,
    validate_url_with_params
)
from . import consts
from .vendored_sdks.models import (
    FluxConfiguration,
    GitRepositoryDefinition,
    RepositoryRefDefinition,
)


def flux_config_show(client, resource_group_name, cluster_name, cluster_type, name):
    """Get an existing Kubernetes Source Control Configuration.

    """
    # Determine ClusterRP
    cluster_rp = get_cluster_type(cluster_type)

    try:
        config = client.get(resource_group_name, cluster_rp, cluster_type, cluster_name, name)
        print(config)
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
                message = '(ConfigurationNotFound) The Resource {0}/{1}/{2}/Microsoft.KubernetesConfiguration/' \
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
def flux_config_create(cmd, client, resource_group_name, cluster_name, name, cluster_type, url=None,
                       scope='cluster', namespace='default', kind=consts.GIT, timeout=None, sync_interval=None,
                       branch=None, tag=None, semver=None, commit=None, auth_ref_override=None, ssh_private_key=None,
                       ssh_private_key_file=None, https_user=None, https_key=None, known_hosts=None,
                       known_hosts_file=None, kustomization=None):

    # Pre-Validation
    validate_repository_ref(branch, tag, semver, commit)
    validate_duration("--timeout", timeout)
    validate_duration("--sync-interval", sync_interval)

    if kustomization:
        validate_kustomization_list(kustomization)

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
    validate_cc_registration(cmd)

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

    # Determine ClusterRP
    cluster_rp = get_cluster_type(cluster_type)

    flux_configuration = FluxConfiguration(
        scope=scope,
        namespace=namespace,
        source_kind=dp_source_kind,
        timeout=timeout,
        sync_interval=sync_interval,
        git_repository=git_repository,
        kustomizations=kustomization
    )

    return client.begin_create_or_update(resource_group_name, cluster_rp,
                                         cluster_type, cluster_name, name, flux_configuration)


def flux_config_delete(client, resource_group_name, cluster_name, cluster_type, name):
    cluster_rp = get_cluster_type(cluster_type)
    return client.begin_delete(resource_group_name, cluster_rp, cluster_type, cluster_name, name)


# def flux_create_source(cmd, client, resource_group_name, cluster_name, name, cluster_type, url,
#     scope='cluster', namespace='default', kind='git', timeout=None, sync_interval=None, branch=None, tag=None, semver=None, commit=None, 
#     auth_ref_override=None, ssh_private_key=None, ssh_private_key_file=None, https_user=None, https_key=None,
#     ssh_known_hosts=None, ssh_known_hosts_file=None):

#     # Determine ClusterRP
#     cluster_rp = get_cluster_type(cluster_type)

#     repository_ref = RepositoryRefDefinition(
#         branch=branch,
#         tag=tag,
#         semver=semver,
#         commit=commit
#     )

#     git_repository = GitRepositoryDefinition(
#         url=url,
#         timeout=timeout,
#         sync_interval=sync_interval,
#         repository_ref=repository_ref,
#         ssh_known_hosts=ssh_known_hosts,
#         https_user=https_user,
#         auth_ref_override=auth_ref_override
#     ) 
    
#     flux_configuration = FluxConfiguration(
#         scope=scope,
#         namespace=namespace,
#         source_kind=kind,
#         timeout=timeout,
#         sync_interval=sync_interval,
#         git_repository=git_repository,
#         kustomizations=[]
#     )
#     # cache the payload if --defer used or send to Azure
#     return cached_put(cmd, client.begin_create_or_update, flux_configuration, resource_group_name, name, cluster_rp, cluster_type, cluster_name)

# def flux_create_kustomization(cmd, client, resource_group_name, cluster_name, config_name, name, cluster_type,
#     dependencies, timeout, sync_interval, retry_interval, path='', prune=False, validation='none', force=False):
    
#     # Determine ClusterRP
#     cluster_rp = get_cluster_type(cluster_type)

#     flux_configuration = cached_get(cmd, client.get, resource_group_name, cluster_rp, cluster_type, cluster_name, config_name)

#     kustomization = KustomizationDefinition(
#         name=name,
#         path=path,
#         dependencies=dependencies,
#         timeout=timeout,
#         sync_interval=sync_interval,
#         retry_interval=retry_interval,
#         prune=prune,
#         validation=validation,
#         force=force
#     )

#     upsert_to_collection(flux_configuration, 'kustomizations', kustomization, 'name')
#     flux_configuration = cached_put(cmd, client.begin_create_or_update, flux_configuration, resource_group_name, name).result()
#     return get_property(flux_configuration.kustomizations, name)
