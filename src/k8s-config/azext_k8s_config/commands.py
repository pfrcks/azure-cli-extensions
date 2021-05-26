# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azext_k8s_config._client_factory import cf_k8s_config_fc_operations


def load_command_table(self, _):
    k8s_config_fc_sdk = CliCommandType(
       operations_tmpl='azext_k8s_config.vendored_sdks.operations#FluxConfigurationsOperations.{}',
       client_factory=cf_k8s_config_fc_operations)

    with self.command_group('k8s-config flux', k8s_config_fc_sdk, is_preview=True) as g:
        g.custom_command('source create', "flux_create_source", supports_local_cache=True)
        g.custom_command('kustomization create', "flux_create_kustomization", supports_local_cache=True)
        g.custom_command('delete', 'flux_delete', confirmation=True)
        g.command('list', "list")
        g.show_command('show', 'get')

