# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from .vendored_sdks.models import (
    FluxConfiguration, 
    GitRepositoryDefinition, 
    KustomizationDefinition,
    RepositoryRefDefinition
)
from .utils import get_cluster_type
from azure.cli.core.commands import cached_get, cached_put, upsert_to_collection, get_property


def flux_create_source(cmd, client, resource_group_name, cluster_name, name, cluster_type, url,
    scope='cluster', namespace='default', kind='git', timeout=None, sync_interval=None, branch=None, tag=None, semver=None, commit=None, 
    auth_ref_override=None, ssh_private_key=None, ssh_private_key_file=None, https_user=None, https_key=None,
    ssh_known_hosts=None, ssh_known_hosts_file=None):

    # Determine ClusterRP
    cluster_rp = get_cluster_type(cluster_type)

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
        ssh_known_hosts=ssh_known_hosts,
        https_user=https_user,
        auth_ref_override=auth_ref_override
    ) 
    
    flux_configuration = FluxConfiguration(
        scope=scope,
        namespace=namespace,
        source_kind=kind,
        timeout=timeout,
        sync_interval=sync_interval,
        git_repository=git_repository,
        kustomizations=[]
    )
    # cache the payload if --defer used or send to Azure
    return cached_put(cmd, client.create_or_update, resource_group_name, cluster_rp, cluster_type, cluster_name, name, flux_configuration)

def flux_create_kustomization(cmd, client, resource_group_name, cluster_name, config_name, name, cluster_type,
    dependencies, timeout, sync_interval, retry_interval, path='', prune=False, validation='none', force=False):
    
    # Determine ClusterRP
    cluster_rp = get_cluster_type(cluster_type)

    flux_configuration = cached_get(cmd, client.get, resource_group_name, cluster_rp, cluster_type, cluster_name, config_name)

    kustomization = KustomizationDefinition(
        name=name,
        path=path,
        dependencies=dependencies,
        timeout=timeout,
        sync_interval=sync_interval,
        retry_interval=retry_interval,
        prune=prune,
        validation=validation,
        force=force
    )

    upsert_to_collection(flux_configuration, 'kustomizations', kustomization, 'name')
    flux_configuration = cached_put(cmd, client.create_or_update, resource_group_name, cluster_rp, cluster_type, cluster_name, name, flux_configuration).result()
    return get_property(flux_configuration.kustomizations, name)

def flux_delete(client, resource_group_name, cluster_name, name, cluster_type):
    raise CLIError('TODO: Implement `k8s-config create`')
