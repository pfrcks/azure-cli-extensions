# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=unused-argument

import datetime
import json

from ..utils import get_cluster_rp_api_version

from knack.log import get_logger

from azure.cli.core.azclierror import InvalidArgumentValueError
from azure.cli.core.commands.client_factory import get_subscription_id
from msrestazure.azure_exceptions import CloudError

from ..vendored_sdks.models import Extension

from .DefaultExtension import DefaultExtension

from .._client_factory import (
    cf_resources)

logger = get_logger(__name__)


class AzureBackupAgent(DefaultExtension):
    def __init__(self):
        # constants for configuration settings.
        self.DEFAULT_RELEASE_NAMESPACE = 'backupagent-ns'

    def Create(self, cmd, client, resource_group_name, cluster_name, name, cluster_type, extension_type,
               scope, auto_upgrade_minor_version, release_train, version, target_namespace,
               release_namespace, configuration_settings, configuration_protected_settings,
               configuration_settings_file, configuration_protected_settings_file):


        # get the arc's location
        subscription_id = get_subscription_id(cmd.cli_ctx)
        cluster_rp, parent_api_version = get_cluster_rp_api_version(cluster_type)
        cluster_resource_id = '/subscriptions/{0}/resourceGroups/{1}/providers/{2}' \
            '/{3}/{4}'.format(subscription_id, resource_group_name, cluster_rp, cluster_type, cluster_name)
        cluster_location = ''
        resources = cf_resources(cmd.cli_ctx, subscription_id)
        try:
            resource = resources.get_by_id(
                cluster_resource_id, parent_api_version)
            cluster_location = resource.location.lower()
        except CloudError as ex:
            raise ex

        # generate values for the extension if none is set.
        configuration_settings['cluster_name'] = configuration_settings.get('cluster_name', cluster_resource_id)
        configuration_settings['extension_name'] = configuration_settings.get('extension_name', name)
        configuration_settings['location'] = configuration_settings.get('location', cluster_location)

        create_identity = True
        extension = Extension(
            extension_type=extension_type,
            auto_upgrade_minor_version=auto_upgrade_minor_version,
            release_train=release_train,
            target_namespace=target_namespace,
            version=version,
            scope=scope,
            configuration_settings=configuration_settings,
            configuration_protected_settings=configuration_protected_settings,
        )
        return extension, name, create_identity
