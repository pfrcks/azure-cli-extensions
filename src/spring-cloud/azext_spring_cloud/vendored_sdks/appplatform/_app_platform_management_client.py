# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from msrest import Deserializer, Serializer

from ._configuration import AppPlatformManagementClientConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential
    from azure.core.pipeline.transport import HttpRequest, HttpResponse

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class AppPlatformManagementClient(MultiApiClientMixin, _SDKClient):
    """REST API for Azure Spring Cloud.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Gets subscription ID which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: API version to use if no profile is provided, or if missing in profile.
    :type api_version: str
    :param base_url: Service URL
    :type base_url: str
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    DEFAULT_API_VERSION = '2020-07-01'
    _PROFILE_TAG = "azure.mgmt.appplatform.AppPlatformManagementClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
            'sku': '2019-05-01-preview',
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        api_version=None, # type: Optional[str]
        base_url=None,  # type: Optional[str]
        profile=KnownProfiles.default, # type: KnownProfiles
        **kwargs  # type: Any
    ):
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = AppPlatformManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(AppPlatformManagementClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2019-05-01-preview: :mod:`v2019_05_01_preview.models<azure.mgmt.appplatform.v2019_05_01_preview.models>`
           * 2020-07-01: :mod:`v2020_07_01.models<azure.mgmt.appplatform.v2020_07_01.models>`
           * 2020-11-01-preview: :mod:`v2020_11_01_preview.models<azure.mgmt.appplatform.v2020_11_01_preview.models>`
           * 2021-06-01-preview: :mod:`v2021_06_01_preview.models<azure.mgmt.appplatform.v2021_06_01_preview.models>`
           * 2021-09-01-preview: :mod:`v2021_09_01_preview.models<azure.mgmt.appplatform.v2021_09_01_preview.models>`
           * 2022-01-01-preview: :mod:`v2022_01_01_preview.models<azure.mgmt.appplatform.v2022_01_01_preview.models>`
        """
        if api_version == '2019-05-01-preview':
            from .v2019_05_01_preview import models
            return models
        elif api_version == '2020-07-01':
            from .v2020_07_01 import models
            return models
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview import models
            return models
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview import models
            return models
        elif api_version == '2021-09-01-preview':
            from .v2021_09_01_preview import models
            return models
        elif api_version == '2022-01-01-preview':
            from .v2022_01_01_preview import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def api_portal_custom_domains(self):
        """Instance depends on the API version:

           * 2022-01-01-preview: :class:`ApiPortalCustomDomainsOperations<azure.mgmt.appplatform.v2022_01_01_preview.operations.ApiPortalCustomDomainsOperations>`
        """
        api_version = self._get_api_version('api_portal_custom_domains')
        if api_version == '2022-01-01-preview':
            from .v2022_01_01_preview.operations import ApiPortalCustomDomainsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'api_portal_custom_domains'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def api_portals(self):
        """Instance depends on the API version:

           * 2022-01-01-preview: :class:`ApiPortalsOperations<azure.mgmt.appplatform.v2022_01_01_preview.operations.ApiPortalsOperations>`
        """
        api_version = self._get_api_version('api_portals')
        if api_version == '2022-01-01-preview':
            from .v2022_01_01_preview.operations import ApiPortalsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'api_portals'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def apps(self):
        """Instance depends on the API version:

           * 2019-05-01-preview: :class:`AppsOperations<azure.mgmt.appplatform.v2019_05_01_preview.operations.AppsOperations>`
           * 2020-07-01: :class:`AppsOperations<azure.mgmt.appplatform.v2020_07_01.operations.AppsOperations>`
           * 2020-11-01-preview: :class:`AppsOperations<azure.mgmt.appplatform.v2020_11_01_preview.operations.AppsOperations>`
           * 2021-06-01-preview: :class:`AppsOperations<azure.mgmt.appplatform.v2021_06_01_preview.operations.AppsOperations>`
           * 2021-09-01-preview: :class:`AppsOperations<azure.mgmt.appplatform.v2021_09_01_preview.operations.AppsOperations>`
           * 2022-01-01-preview: :class:`AppsOperations<azure.mgmt.appplatform.v2022_01_01_preview.operations.AppsOperations>`
        """
        api_version = self._get_api_version('apps')
        if api_version == '2019-05-01-preview':
            from .v2019_05_01_preview.operations import AppsOperations as OperationClass
        elif api_version == '2020-07-01':
            from .v2020_07_01.operations import AppsOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import AppsOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import AppsOperations as OperationClass
        elif api_version == '2021-09-01-preview':
            from .v2021_09_01_preview.operations import AppsOperations as OperationClass
        elif api_version == '2022-01-01-preview':
            from .v2022_01_01_preview.operations import AppsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'apps'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def bindings(self):
        """Instance depends on the API version:

           * 2019-05-01-preview: :class:`BindingsOperations<azure.mgmt.appplatform.v2019_05_01_preview.operations.BindingsOperations>`
           * 2020-07-01: :class:`BindingsOperations<azure.mgmt.appplatform.v2020_07_01.operations.BindingsOperations>`
           * 2020-11-01-preview: :class:`BindingsOperations<azure.mgmt.appplatform.v2020_11_01_preview.operations.BindingsOperations>`
           * 2021-06-01-preview: :class:`BindingsOperations<azure.mgmt.appplatform.v2021_06_01_preview.operations.BindingsOperations>`
           * 2021-09-01-preview: :class:`BindingsOperations<azure.mgmt.appplatform.v2021_09_01_preview.operations.BindingsOperations>`
           * 2022-01-01-preview: :class:`BindingsOperations<azure.mgmt.appplatform.v2022_01_01_preview.operations.BindingsOperations>`
        """
        api_version = self._get_api_version('bindings')
        if api_version == '2019-05-01-preview':
            from .v2019_05_01_preview.operations import BindingsOperations as OperationClass
        elif api_version == '2020-07-01':
            from .v2020_07_01.operations import BindingsOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import BindingsOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import BindingsOperations as OperationClass
        elif api_version == '2021-09-01-preview':
            from .v2021_09_01_preview.operations import BindingsOperations as OperationClass
        elif api_version == '2022-01-01-preview':
            from .v2022_01_01_preview.operations import BindingsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'bindings'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def build_service(self):
        """Instance depends on the API version:

           * 2022-01-01-preview: :class:`BuildServiceOperations<azure.mgmt.appplatform.v2022_01_01_preview.operations.BuildServiceOperations>`
        """
        api_version = self._get_api_version('build_service')
        if api_version == '2022-01-01-preview':
            from .v2022_01_01_preview.operations import BuildServiceOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'build_service'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def build_service_agent_pool(self):
        """Instance depends on the API version:

           * 2022-01-01-preview: :class:`BuildServiceAgentPoolOperations<azure.mgmt.appplatform.v2022_01_01_preview.operations.BuildServiceAgentPoolOperations>`
        """
        api_version = self._get_api_version('build_service_agent_pool')
        if api_version == '2022-01-01-preview':
            from .v2022_01_01_preview.operations import BuildServiceAgentPoolOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'build_service_agent_pool'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def build_service_builder(self):
        """Instance depends on the API version:

           * 2022-01-01-preview: :class:`BuildServiceBuilderOperations<azure.mgmt.appplatform.v2022_01_01_preview.operations.BuildServiceBuilderOperations>`
        """
        api_version = self._get_api_version('build_service_builder')
        if api_version == '2022-01-01-preview':
            from .v2022_01_01_preview.operations import BuildServiceBuilderOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'build_service_builder'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def buildpack_binding(self):
        """Instance depends on the API version:

           * 2022-01-01-preview: :class:`BuildpackBindingOperations<azure.mgmt.appplatform.v2022_01_01_preview.operations.BuildpackBindingOperations>`
        """
        api_version = self._get_api_version('buildpack_binding')
        if api_version == '2022-01-01-preview':
            from .v2022_01_01_preview.operations import BuildpackBindingOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'buildpack_binding'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def certificates(self):
        """Instance depends on the API version:

           * 2019-05-01-preview: :class:`CertificatesOperations<azure.mgmt.appplatform.v2019_05_01_preview.operations.CertificatesOperations>`
           * 2020-07-01: :class:`CertificatesOperations<azure.mgmt.appplatform.v2020_07_01.operations.CertificatesOperations>`
           * 2020-11-01-preview: :class:`CertificatesOperations<azure.mgmt.appplatform.v2020_11_01_preview.operations.CertificatesOperations>`
           * 2021-06-01-preview: :class:`CertificatesOperations<azure.mgmt.appplatform.v2021_06_01_preview.operations.CertificatesOperations>`
           * 2021-09-01-preview: :class:`CertificatesOperations<azure.mgmt.appplatform.v2021_09_01_preview.operations.CertificatesOperations>`
           * 2022-01-01-preview: :class:`CertificatesOperations<azure.mgmt.appplatform.v2022_01_01_preview.operations.CertificatesOperations>`
        """
        api_version = self._get_api_version('certificates')
        if api_version == '2019-05-01-preview':
            from .v2019_05_01_preview.operations import CertificatesOperations as OperationClass
        elif api_version == '2020-07-01':
            from .v2020_07_01.operations import CertificatesOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import CertificatesOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import CertificatesOperations as OperationClass
        elif api_version == '2021-09-01-preview':
            from .v2021_09_01_preview.operations import CertificatesOperations as OperationClass
        elif api_version == '2022-01-01-preview':
            from .v2022_01_01_preview.operations import CertificatesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'certificates'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def config_servers(self):
        """Instance depends on the API version:

           * 2020-07-01: :class:`ConfigServersOperations<azure.mgmt.appplatform.v2020_07_01.operations.ConfigServersOperations>`
           * 2020-11-01-preview: :class:`ConfigServersOperations<azure.mgmt.appplatform.v2020_11_01_preview.operations.ConfigServersOperations>`
           * 2021-06-01-preview: :class:`ConfigServersOperations<azure.mgmt.appplatform.v2021_06_01_preview.operations.ConfigServersOperations>`
           * 2021-09-01-preview: :class:`ConfigServersOperations<azure.mgmt.appplatform.v2021_09_01_preview.operations.ConfigServersOperations>`
           * 2022-01-01-preview: :class:`ConfigServersOperations<azure.mgmt.appplatform.v2022_01_01_preview.operations.ConfigServersOperations>`
        """
        api_version = self._get_api_version('config_servers')
        if api_version == '2020-07-01':
            from .v2020_07_01.operations import ConfigServersOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import ConfigServersOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import ConfigServersOperations as OperationClass
        elif api_version == '2021-09-01-preview':
            from .v2021_09_01_preview.operations import ConfigServersOperations as OperationClass
        elif api_version == '2022-01-01-preview':
            from .v2022_01_01_preview.operations import ConfigServersOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'config_servers'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def configuration_services(self):
        """Instance depends on the API version:

           * 2022-01-01-preview: :class:`ConfigurationServicesOperations<azure.mgmt.appplatform.v2022_01_01_preview.operations.ConfigurationServicesOperations>`
        """
        api_version = self._get_api_version('configuration_services')
        if api_version == '2022-01-01-preview':
            from .v2022_01_01_preview.operations import ConfigurationServicesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'configuration_services'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def custom_domains(self):
        """Instance depends on the API version:

           * 2019-05-01-preview: :class:`CustomDomainsOperations<azure.mgmt.appplatform.v2019_05_01_preview.operations.CustomDomainsOperations>`
           * 2020-07-01: :class:`CustomDomainsOperations<azure.mgmt.appplatform.v2020_07_01.operations.CustomDomainsOperations>`
           * 2020-11-01-preview: :class:`CustomDomainsOperations<azure.mgmt.appplatform.v2020_11_01_preview.operations.CustomDomainsOperations>`
           * 2021-06-01-preview: :class:`CustomDomainsOperations<azure.mgmt.appplatform.v2021_06_01_preview.operations.CustomDomainsOperations>`
           * 2021-09-01-preview: :class:`CustomDomainsOperations<azure.mgmt.appplatform.v2021_09_01_preview.operations.CustomDomainsOperations>`
           * 2022-01-01-preview: :class:`CustomDomainsOperations<azure.mgmt.appplatform.v2022_01_01_preview.operations.CustomDomainsOperations>`
        """
        api_version = self._get_api_version('custom_domains')
        if api_version == '2019-05-01-preview':
            from .v2019_05_01_preview.operations import CustomDomainsOperations as OperationClass
        elif api_version == '2020-07-01':
            from .v2020_07_01.operations import CustomDomainsOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import CustomDomainsOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import CustomDomainsOperations as OperationClass
        elif api_version == '2021-09-01-preview':
            from .v2021_09_01_preview.operations import CustomDomainsOperations as OperationClass
        elif api_version == '2022-01-01-preview':
            from .v2022_01_01_preview.operations import CustomDomainsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'custom_domains'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def deployments(self):
        """Instance depends on the API version:

           * 2019-05-01-preview: :class:`DeploymentsOperations<azure.mgmt.appplatform.v2019_05_01_preview.operations.DeploymentsOperations>`
           * 2020-07-01: :class:`DeploymentsOperations<azure.mgmt.appplatform.v2020_07_01.operations.DeploymentsOperations>`
           * 2020-11-01-preview: :class:`DeploymentsOperations<azure.mgmt.appplatform.v2020_11_01_preview.operations.DeploymentsOperations>`
           * 2021-06-01-preview: :class:`DeploymentsOperations<azure.mgmt.appplatform.v2021_06_01_preview.operations.DeploymentsOperations>`
           * 2021-09-01-preview: :class:`DeploymentsOperations<azure.mgmt.appplatform.v2021_09_01_preview.operations.DeploymentsOperations>`
           * 2022-01-01-preview: :class:`DeploymentsOperations<azure.mgmt.appplatform.v2022_01_01_preview.operations.DeploymentsOperations>`
        """
        api_version = self._get_api_version('deployments')
        if api_version == '2019-05-01-preview':
            from .v2019_05_01_preview.operations import DeploymentsOperations as OperationClass
        elif api_version == '2020-07-01':
            from .v2020_07_01.operations import DeploymentsOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import DeploymentsOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import DeploymentsOperations as OperationClass
        elif api_version == '2021-09-01-preview':
            from .v2021_09_01_preview.operations import DeploymentsOperations as OperationClass
        elif api_version == '2022-01-01-preview':
            from .v2022_01_01_preview.operations import DeploymentsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'deployments'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def gateway_custom_domains(self):
        """Instance depends on the API version:

           * 2022-01-01-preview: :class:`GatewayCustomDomainsOperations<azure.mgmt.appplatform.v2022_01_01_preview.operations.GatewayCustomDomainsOperations>`
        """
        api_version = self._get_api_version('gateway_custom_domains')
        if api_version == '2022-01-01-preview':
            from .v2022_01_01_preview.operations import GatewayCustomDomainsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'gateway_custom_domains'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def gateway_route_configs(self):
        """Instance depends on the API version:

           * 2022-01-01-preview: :class:`GatewayRouteConfigsOperations<azure.mgmt.appplatform.v2022_01_01_preview.operations.GatewayRouteConfigsOperations>`
        """
        api_version = self._get_api_version('gateway_route_configs')
        if api_version == '2022-01-01-preview':
            from .v2022_01_01_preview.operations import GatewayRouteConfigsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'gateway_route_configs'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def gateways(self):
        """Instance depends on the API version:

           * 2022-01-01-preview: :class:`GatewaysOperations<azure.mgmt.appplatform.v2022_01_01_preview.operations.GatewaysOperations>`
        """
        api_version = self._get_api_version('gateways')
        if api_version == '2022-01-01-preview':
            from .v2022_01_01_preview.operations import GatewaysOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'gateways'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def monitoring_settings(self):
        """Instance depends on the API version:

           * 2020-07-01: :class:`MonitoringSettingsOperations<azure.mgmt.appplatform.v2020_07_01.operations.MonitoringSettingsOperations>`
           * 2020-11-01-preview: :class:`MonitoringSettingsOperations<azure.mgmt.appplatform.v2020_11_01_preview.operations.MonitoringSettingsOperations>`
           * 2021-06-01-preview: :class:`MonitoringSettingsOperations<azure.mgmt.appplatform.v2021_06_01_preview.operations.MonitoringSettingsOperations>`
           * 2021-09-01-preview: :class:`MonitoringSettingsOperations<azure.mgmt.appplatform.v2021_09_01_preview.operations.MonitoringSettingsOperations>`
           * 2022-01-01-preview: :class:`MonitoringSettingsOperations<azure.mgmt.appplatform.v2022_01_01_preview.operations.MonitoringSettingsOperations>`
        """
        api_version = self._get_api_version('monitoring_settings')
        if api_version == '2020-07-01':
            from .v2020_07_01.operations import MonitoringSettingsOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import MonitoringSettingsOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import MonitoringSettingsOperations as OperationClass
        elif api_version == '2021-09-01-preview':
            from .v2021_09_01_preview.operations import MonitoringSettingsOperations as OperationClass
        elif api_version == '2022-01-01-preview':
            from .v2022_01_01_preview.operations import MonitoringSettingsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'monitoring_settings'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2019-05-01-preview: :class:`Operations<azure.mgmt.appplatform.v2019_05_01_preview.operations.Operations>`
           * 2020-07-01: :class:`Operations<azure.mgmt.appplatform.v2020_07_01.operations.Operations>`
           * 2020-11-01-preview: :class:`Operations<azure.mgmt.appplatform.v2020_11_01_preview.operations.Operations>`
           * 2021-06-01-preview: :class:`Operations<azure.mgmt.appplatform.v2021_06_01_preview.operations.Operations>`
           * 2021-09-01-preview: :class:`Operations<azure.mgmt.appplatform.v2021_09_01_preview.operations.Operations>`
           * 2022-01-01-preview: :class:`Operations<azure.mgmt.appplatform.v2022_01_01_preview.operations.Operations>`
        """
        api_version = self._get_api_version('operations')
        if api_version == '2019-05-01-preview':
            from .v2019_05_01_preview.operations import Operations as OperationClass
        elif api_version == '2020-07-01':
            from .v2020_07_01.operations import Operations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import Operations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import Operations as OperationClass
        elif api_version == '2021-09-01-preview':
            from .v2021_09_01_preview.operations import Operations as OperationClass
        elif api_version == '2022-01-01-preview':
            from .v2022_01_01_preview.operations import Operations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'operations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def runtime_versions(self):
        """Instance depends on the API version:

           * 2019-05-01-preview: :class:`RuntimeVersionsOperations<azure.mgmt.appplatform.v2019_05_01_preview.operations.RuntimeVersionsOperations>`
           * 2020-07-01: :class:`RuntimeVersionsOperations<azure.mgmt.appplatform.v2020_07_01.operations.RuntimeVersionsOperations>`
           * 2020-11-01-preview: :class:`RuntimeVersionsOperations<azure.mgmt.appplatform.v2020_11_01_preview.operations.RuntimeVersionsOperations>`
           * 2021-06-01-preview: :class:`RuntimeVersionsOperations<azure.mgmt.appplatform.v2021_06_01_preview.operations.RuntimeVersionsOperations>`
           * 2021-09-01-preview: :class:`RuntimeVersionsOperations<azure.mgmt.appplatform.v2021_09_01_preview.operations.RuntimeVersionsOperations>`
           * 2022-01-01-preview: :class:`RuntimeVersionsOperations<azure.mgmt.appplatform.v2022_01_01_preview.operations.RuntimeVersionsOperations>`
        """
        api_version = self._get_api_version('runtime_versions')
        if api_version == '2019-05-01-preview':
            from .v2019_05_01_preview.operations import RuntimeVersionsOperations as OperationClass
        elif api_version == '2020-07-01':
            from .v2020_07_01.operations import RuntimeVersionsOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import RuntimeVersionsOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import RuntimeVersionsOperations as OperationClass
        elif api_version == '2021-09-01-preview':
            from .v2021_09_01_preview.operations import RuntimeVersionsOperations as OperationClass
        elif api_version == '2022-01-01-preview':
            from .v2022_01_01_preview.operations import RuntimeVersionsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'runtime_versions'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def service_registries(self):
        """Instance depends on the API version:

           * 2022-01-01-preview: :class:`ServiceRegistriesOperations<azure.mgmt.appplatform.v2022_01_01_preview.operations.ServiceRegistriesOperations>`
        """
        api_version = self._get_api_version('service_registries')
        if api_version == '2022-01-01-preview':
            from .v2022_01_01_preview.operations import ServiceRegistriesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'service_registries'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def services(self):
        """Instance depends on the API version:

           * 2019-05-01-preview: :class:`ServicesOperations<azure.mgmt.appplatform.v2019_05_01_preview.operations.ServicesOperations>`
           * 2020-07-01: :class:`ServicesOperations<azure.mgmt.appplatform.v2020_07_01.operations.ServicesOperations>`
           * 2020-11-01-preview: :class:`ServicesOperations<azure.mgmt.appplatform.v2020_11_01_preview.operations.ServicesOperations>`
           * 2021-06-01-preview: :class:`ServicesOperations<azure.mgmt.appplatform.v2021_06_01_preview.operations.ServicesOperations>`
           * 2021-09-01-preview: :class:`ServicesOperations<azure.mgmt.appplatform.v2021_09_01_preview.operations.ServicesOperations>`
           * 2022-01-01-preview: :class:`ServicesOperations<azure.mgmt.appplatform.v2022_01_01_preview.operations.ServicesOperations>`
        """
        api_version = self._get_api_version('services')
        if api_version == '2019-05-01-preview':
            from .v2019_05_01_preview.operations import ServicesOperations as OperationClass
        elif api_version == '2020-07-01':
            from .v2020_07_01.operations import ServicesOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import ServicesOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import ServicesOperations as OperationClass
        elif api_version == '2021-09-01-preview':
            from .v2021_09_01_preview.operations import ServicesOperations as OperationClass
        elif api_version == '2022-01-01-preview':
            from .v2022_01_01_preview.operations import ServicesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'services'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def sku(self):
        """Instance depends on the API version:

           * 2019-05-01-preview: :class:`SkuOperations<azure.mgmt.appplatform.v2019_05_01_preview.operations.SkuOperations>`
        """
        api_version = self._get_api_version('sku')
        if api_version == '2019-05-01-preview':
            from .v2019_05_01_preview.operations import SkuOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'sku'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def skus(self):
        """Instance depends on the API version:

           * 2020-07-01: :class:`SkusOperations<azure.mgmt.appplatform.v2020_07_01.operations.SkusOperations>`
           * 2020-11-01-preview: :class:`SkusOperations<azure.mgmt.appplatform.v2020_11_01_preview.operations.SkusOperations>`
           * 2021-06-01-preview: :class:`SkusOperations<azure.mgmt.appplatform.v2021_06_01_preview.operations.SkusOperations>`
           * 2021-09-01-preview: :class:`SkusOperations<azure.mgmt.appplatform.v2021_09_01_preview.operations.SkusOperations>`
           * 2022-01-01-preview: :class:`SkusOperations<azure.mgmt.appplatform.v2022_01_01_preview.operations.SkusOperations>`
        """
        api_version = self._get_api_version('skus')
        if api_version == '2020-07-01':
            from .v2020_07_01.operations import SkusOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import SkusOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import SkusOperations as OperationClass
        elif api_version == '2021-09-01-preview':
            from .v2021_09_01_preview.operations import SkusOperations as OperationClass
        elif api_version == '2022-01-01-preview':
            from .v2022_01_01_preview.operations import SkusOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'skus'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def storages(self):
        """Instance depends on the API version:

           * 2021-09-01-preview: :class:`StoragesOperations<azure.mgmt.appplatform.v2021_09_01_preview.operations.StoragesOperations>`
           * 2022-01-01-preview: :class:`StoragesOperations<azure.mgmt.appplatform.v2022_01_01_preview.operations.StoragesOperations>`
        """
        api_version = self._get_api_version('storages')
        if api_version == '2021-09-01-preview':
            from .v2021_09_01_preview.operations import StoragesOperations as OperationClass
        elif api_version == '2022-01-01-preview':
            from .v2022_01_01_preview.operations import StoragesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'storages'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    def close(self):
        self._client.close()
    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)
