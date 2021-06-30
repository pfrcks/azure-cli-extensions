# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from .providers.ExtensionProvider import ExtensionProvider
from .providers.FluxConfigurationProvider import FluxConfigurationProvider
from .utils import get_cluster_rp
from . import consts

from .vendored_sdks.v2021_06_01_preview.models import (
    RepositoryRefDefinition,
    GitRepositoryDefinition,
    FluxConfiguration
)

# Flux Configuration Methods

def flux_config_show(cmd, client, resource_group_name, cluster_type, cluster_name, name):
    provider = FluxConfigurationProvider(cmd)
    return provider.show(resource_group_name, cluster_type, cluster_name, name)


# pylint: disable=too-many-locals
def flux_config_create(cmd, client, resource_group_name, cluster_type, cluster_name, name, url=None,
                       scope='cluster', namespace='default', kind=consts.GIT, timeout=None, sync_interval=None,
                       branch=None, tag=None, semver=None, commit=None, local_auth_ref=None, ssh_private_key=None,
                       ssh_private_key_file=None, https_user=None, https_key=None, known_hosts=None,
                       known_hosts_file=None, kustomization=None):

    provider = FluxConfigurationProvider(cmd)
    return provider.create(resource_group_name, cluster_type, cluster_name, name, url, scope, namespace, kind, timeout, sync_interval,
                           branch, tag, semver, commit, local_auth_ref, ssh_private_key,
                           ssh_private_key_file, https_user, https_key, known_hosts,
                           known_hosts_file, kustomization)


def flux_config_create_source(cmd, client, resource_group_name, cluster_type, cluster_name, name, url=None,
                              scope='cluster', namespace='default', kind=consts.GIT, timeout=None, sync_interval=None,
                              branch=None, tag=None, semver=None, commit=None, local_auth_ref=None, ssh_private_key=None,
                              ssh_private_key_file=None, https_user=None, https_key=None, known_hosts=None,
                              known_hosts_file=None):
    
    provider = FluxConfigurationProvider(cmd)
    return provider.create_source(resource_group_name, cluster_type, cluster_name, name, url, scope, namespace, kind, timeout, sync_interval,
                                  branch, tag, semver, commit, local_auth_ref, ssh_private_key,
                                  ssh_private_key_file, https_user, https_key, known_hosts,
                                  known_hosts_file)

def flux_config_create_kustomization(cmd, client, resource_group_name, cluster_name, config_name, name, cluster_type,
                                     dependencies=None, timeout=None, sync_interval=None, retry_interval=None, path='', prune=False, validation='none', force=False):
    
    provider = FluxConfigurationProvider(cmd)
    return provider.create_kustomization(resource_group_name, cluster_name, config_name, name, cluster_type,
                                     dependencies, timeout, sync_interval, retry_interval, path, prune, validation, force)

def flux_config_delete(cmd, client, resource_group_name, cluster_type, cluster_name, name):
    provider = FluxConfigurationProvider(cmd)
    return provider.delete(resource_group_name, cluster_type, cluster_name, name)


# Extension Methods

def extension_show(cmd, client, resource_group_name, cluster_type, cluster_name, name):
    provider = ExtensionProvider(cmd)
    return provider.show(resource_group_name, cluster_type, cluster_name, name)


def extension_list(cmd, client, resource_group_name, cluster_type, cluster_name):
    provider = ExtensionProvider(cmd)
    return provider.list(resource_group_name, cluster_type, cluster_name)


def extension_create(cmd, client, resource_group_name, cluster_type, cluster_name, name,
                     extension_type, scope=None, auto_upgrade_minor_version=None, release_train=None,
                     version=None, target_namespace=None, release_namespace=None, configuration_settings=None,
                     configuration_protected_settings=None, configuration_settings_file=None,
                     configuration_protected_settings_file=None, tags=None):
    provider = ExtensionProvider(cmd)
    return provider.create(resource_group_name, cluster_type, cluster_name, name, extension_type, scope, auto_upgrade_minor_version, release_train, version, target_namespace, release_namespace,
                    configuration_settings, configuration_protected_settings, configuration_settings_file, configuration_protected_settings_file)


def extension_delete(cmd, client, resource_group_name, cluster_type, cluster_name, name):
    provider = ExtensionProvider(cmd)
    return provider.delete(resource_group_name, cluster_type, cluster_name, name)

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
