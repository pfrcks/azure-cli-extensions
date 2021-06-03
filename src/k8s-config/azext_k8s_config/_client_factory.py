# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands.client_factory import get_mgmt_service_client


def k8s_config_client(cli_ctx, *_):
    from azext_k8s_config.vendored_sdks import SourceControlConfigurationClient
    return get_mgmt_service_client(cli_ctx, SourceControlConfigurationClient)


def k8s_config_fluxconfig_client(cli_ctx, *_):
    return k8s_config_client(cli_ctx).flux_configurations


def k8s_config_sourcecontrol_client(cli_ctx, *_):
    return k8s_config_client(cli_ctx).source_control_configurations


def k8s_config_extension_client(cli_ctx, *_):
    return k8s_config_client(cli_ctx).extensions


def resource_providers_client(cli_ctx):
    from azure.mgmt.resource import ResourceManagementClient
    return get_mgmt_service_client(cli_ctx, ResourceManagementClient).providers
