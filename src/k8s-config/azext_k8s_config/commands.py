# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azext_k8s_config._client_factory import (
    k8s_config_fluxconfig_client,
    k8s_config_extension_client
)
from .format import (
    fluxconfig_list_table_format,
    fluxconfig_show_table_format,
    extension_list_table_format,
    extension_show_table_format
)


def load_command_table(self, _):
    k8s_config_fluxconfig_sdk = CliCommandType(
        operations_tmpl='azext_k8s_config.vendored_sdks.operations#FluxConfigurationsOperations.{}',
        client_factory=k8s_config_fluxconfig_client
    )

    k8s_config_extension_sdk = CliCommandType(
        operations_tmpl='azext_k8s_config.vendored_sdks.operations#ExtensionsOperations.{}',
        client_factory=k8s_config_extension_client
    )

    with self.command_group('k8s-config flux', k8s_config_fluxconfig_sdk, client_factory=k8s_config_fluxconfig_client, is_experimental=True) as g:
        g.custom_command('create', 'flux_config_create', supports_no_wait=True)
        g.custom_command('list', "flux_config_list", table_transformer=fluxconfig_list_table_format)
        g.custom_command('show', 'flux_config_show', table_transformer=fluxconfig_show_table_format)
        g.custom_command('delete', 'flux_config_delete', confirmation=True, supports_no_wait=True)
        # g.custom_command('source create', 'flux_config_create_source', supports_local_cache=True)
        # g.custom_command('kustomization create', 'flux_config_create_kustomization', supports_local_cache=True)

    with self.command_group('k8s-config extension', k8s_config_extension_sdk, client_factory=k8s_config_extension_client, is_preview=True) as g:
        g.custom_command('create', 'extension_create', supports_no_wait=True)
        g.custom_command('list', "extension_list", table_transformer=extension_list_table_format)
        g.custom_command('show', 'extension_show', table_transformer=extension_show_table_format)
        g.custom_command('delete', 'extension_delete', confirmation=True, supports_no_wait=True)
