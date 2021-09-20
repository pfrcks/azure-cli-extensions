# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=unused-argument

from knack.util import CLIError
from knack.log import get_logger

from ..vendored_sdks.models import Extension
from ..vendored_sdks.models import ScopeCluster
from ..vendored_sdks.models import Scope

from .PartnerExtensionModel import PartnerExtensionModel

logger = get_logger(__name__)


class AzurePolicy(PartnerExtensionModel):
    def Create(self, cmd, client, resource_group_name, cluster_name, name, cluster_type, extension_type,
               scope, auto_upgrade_minor_version, release_train, version, target_namespace,
               release_namespace, configuration_settings, configuration_protected_settings,
               configuration_settings_file, configuration_protected_settings_file):

        """ExtensionType 'Microsoft.PolicyInsights' specific validations & defaults for Create
           Must create and return a valid 'ExtensionInstance' object.

        """

        # Hardcode scope to cluster
        ext_scope = None
        scope_cluster = ScopeCluster(release_namespace=release_namespace)
        ext_scope = Scope(cluster=scope_cluster, namespace=None)
        logger.warning('Ignoring scope parameters since %s '
                       'only supports cluster scope', extension_type)

        # If release-train is not provided, set it to 'preview'
        valid_release_trains = ['preview', 'dev']
        if release_train is None:
            release_train = 'preview'

        # If release-train is other than valid_release_trains raise error
        if release_train.lower() not in valid_release_trains:
            raise CLIError("Invalid release-train '{}'.  Valid values are 'preview', 'dev'.".format(release_train))

        # Create Managed Identity for extension
        create_identity = True

        extension_instance = Extension(
            extension_type=extension_type,
            auto_upgrade_minor_version=auto_upgrade_minor_version,
            release_train=release_train,
            version=version,
            scope=ext_scope,
            configuration_settings=configuration_settings,
            configuration_protected_settings=configuration_protected_settings,
        )
        return extension_instance, name, create_identity

    def Update(self, extension, auto_upgrade_minor_version, release_train, version):
        """ExtensionType 'Microsoft.PolicyInsights' specific validations & defaults for Update
           Must create and return a valid 'Extension' object.

        """
        # If release-train is not provided, set it to 'preview'
        valid_release_trains = ['preview', 'dev']
        if release_train is None:
            release_train = 'preview'

        # If release-train is other than valid_release_trains raise error
        if release_train.lower() not in valid_release_trains:
            raise CLIError("Invalid release-train '{}'.  Valid values are 'preview', 'dev'.".format(release_train))

        return Extension(
            auto_upgrade_minor_version=auto_upgrade_minor_version,
            release_train=release_train,
            version=version
        )

    def Delete(self, client, resource_group_name, cluster_name, name, cluster_type):
        pass