# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=unused-argument,too-many-locals

from knack.log import get_logger

from msrestazure.azure_exceptions import CloudError

from azure.cli.core.azclierror import ResourceNotFoundError, MutuallyExclusiveArgumentError, \
    InvalidArgumentValueError, CommandNotFoundError, RequiredArgumentMissingError
from azure.cli.core.commands.client_factory import get_subscription_id
from ..vendored_sdks.models import Identity
from ..vendored_sdks.models import Scope

from ..partner_extensions.ContainerInsights import ContainerInsights
from ..partner_extensions.AzureDefender import AzureDefender
from ..partner_extensions.Cassandra import Cassandra
from ..partner_extensions.AzureMLKubernetes import AzureMLKubernetes
from ..partner_extensions.DefaultExtension import DefaultExtension
from ..utils import get_cluster_rp, read_config_settings_file

from .._client_factory import cf_resources

logger = get_logger(__name__)


# A factory method to return the correct extension class based off of the extension name
def ExtensionFactory(extension_name):
    extension_map = {
        'microsoft.azuremonitor.containers': ContainerInsights,
        'microsoft.azuredefender.kubernetes': AzureDefender,
        'microsoft.azureml.kubernetes': AzureMLKubernetes,
        'cassandradatacentersoperator': Cassandra,
    }

    # Return the extension if we find it in the map, else return the default
    return extension_map.get(extension_name, DefaultExtension)()


class ExtensionProvider:
    def __init__(self, cmd, client, resource_group_name, cluster_name, cluster_type, name=None):
        self.cmd = cmd
        self.client = client
        self.resource_group_name = resource_group_name
        self.cluster_name = cluster_name
        self.cluster_type = cluster_type
        self.name = name
        self.cluster_rp = get_cluster_rp(cluster_type)


    def create(self, extension_type, scope=None, auto_upgrade_minor_version=None, release_train=None,
               version=None, target_namespace=None, release_namespace=None, configuration_settings=None,
               configuration_protected_settings=None, configuration_settings_file=None,
               configuration_protected_settings_file=None, tags=None):
        """Create a new Extension Instance.

        """
        extension_type_lower = extension_type.lower()

        # Configuration Settings & Configuration Protected Settings
        if configuration_settings is not None and configuration_settings_file is not None:
            raise MutuallyExclusiveArgumentError(
                'Error! Both configuration-settings and configuration-settings-file cannot be provided.'
            )

        if configuration_protected_settings is not None and configuration_protected_settings_file is not None:
            raise MutuallyExclusiveArgumentError(
                'Error! Both configuration-protected-settings and configuration-protected-settings-file '
                'cannot be provided.'
            )

        config_settings = {}
        config_protected_settings = {}
        # Get Configuration Settings from file
        if configuration_settings_file is not None:
            config_settings = read_config_settings_file(configuration_settings_file)

        if configuration_settings is not None:
            for dicts in configuration_settings:
                for key, value in dicts.items():
                    config_settings[key] = value

        # Get Configuration Protected Settings from file
        if configuration_protected_settings_file is not None:
            config_protected_settings = read_config_settings_file(configuration_protected_settings_file)

        if configuration_protected_settings is not None:
            for dicts in configuration_protected_settings:
                for key, value in dicts.items():
                    config_protected_settings[key] = value

        # Identity is not created by default.  Extension type must specify if identity is required.
        create_identity = False
        extension_instance = None

        # Scope & Namespace validation - common to all extension-types
        self.__validate_scope_and_namespace(scope, release_namespace, target_namespace)

        # Give Partners a chance to their extensionType specific validations and to set value over-rides.

        # Get the extension class based on the extension name
        extension_class = ExtensionFactory(extension_type_lower)
        extension_instance, name, create_identity = extension_class.Create(
            self.cmd, self.client, self.resource_group_name, self.cluster_name, self.name, self.cluster_type, extension_type_lower, scope,
            auto_upgrade_minor_version, release_train, version, target_namespace, release_namespace, config_settings,
            config_protected_settings, configuration_settings_file, configuration_protected_settings_file)

        # Common validations
        self.__validate_version_and_auto_upgrade(extension_instance.version, extension_instance.auto_upgrade_minor_version)
        self.__validate_scope_after_customization(extension_instance.scope)

        # Create identity, if required
        if create_identity:
            extension_instance.identity, extension_instance.location = self.__create_identity()

        # Try to create the resource
        return self.client.create(self.resource_group_name, self.cluster_rp, self.cluster_type, self.cluster_name, name, extension_instance)

    def __validate_scope_and_namespace(scope, release_namespace, target_namespace):
        if scope == 'cluster':
            if target_namespace is not None:
                message = "When --scope is 'cluster', --target-namespace must not be given."
                raise MutuallyExclusiveArgumentError(message)
        else:
            if release_namespace is not None:
                message = "When --scope is 'namespace', --release-namespace must not be given."
                raise MutuallyExclusiveArgumentError(message)


    def __validate_scope_after_customization(self, scope_obj):
        if scope_obj is not None and scope_obj.namespace is not None and scope_obj.namespace.target_namespace is None:
            message = "When --scope is 'namespace', --target-namespace must be given."
            raise RequiredArgumentMissingError(message)


    def __validate_version_and_auto_upgrade(self, version, auto_upgrade_minor_version):
        if version is not None:
            if auto_upgrade_minor_version:
                message = "To pin to specific version, auto-upgrade-minor-version must be set to 'false'."
                raise MutuallyExclusiveArgumentError(message)

            auto_upgrade_minor_version = False
    

    def __create_identity(self):
        subscription_id = get_subscription_id(self.cmd.cli_ctx)
        resources = cf_resources(self.cmd.cli_ctx, subscription_id)

        cluster_resource_id = '/subscriptions/{0}/resourceGroups/{1}/providers/{2}/{3}/{4}'.format(subscription_id,
                                                                                                   self.resource_group_name,
                                                                                                   self.cluster_rp,
                                                                                                   self.cluster_type,
                                                                                                   self.cluster_name)

        if self.cluster_rp == 'Microsoft.Kubernetes':
            parent_api_version = '2020-01-01-preview'
        elif self.cluster_rp == 'Microsoft.ResourceConnector':
            parent_api_version = '2020-09-15-privatepreview'
        elif self.cluster_rp == 'Microsoft.ContainerService':
            parent_api_version = '2017-07-01'
        else:
            raise InvalidArgumentValueError(
                "Error! Cluster type '{}' is not supported for extension identity".format(self.cluster_type)
            )

        try:
            resource = resources.get_by_id(cluster_resource_id, parent_api_version)
            location = str(resource.location.lower())
        except CloudError as ex:
            raise ex
        identity_type = "SystemAssigned"

        return Identity(type=identity_type), location