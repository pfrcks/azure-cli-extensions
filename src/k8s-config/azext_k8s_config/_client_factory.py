# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def cf_k8s_config(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_k8s_config.vendored_sdks import SourceControlConfigurationClient
    return get_mgmt_service_client(cli_ctx, SourceControlConfigurationClient)


def cf_k8s_config_fc_operations(cli_ctx, _):
    return cf_k8s_config(cli_ctx).flux_configurations
