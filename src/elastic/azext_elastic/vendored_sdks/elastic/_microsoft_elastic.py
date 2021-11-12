# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import MicrosoftElasticConfiguration
from .operations import Operations
from .operations import MonitorsOperations
from .operations import MonitoredResourcesOperations
from .operations import DeploymentInfoOperations
from .operations import TagRulesOperations
from .operations import VmHostOperations
from .operations import VmIngestionOperations
from .operations import VmCollectionOperations
from . import models


class MicrosoftElastic(object):
    """MicrosoftElastic.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.elastic.operations.Operations
    :ivar monitors: MonitorsOperations operations
    :vartype monitors: azure.mgmt.elastic.operations.MonitorsOperations
    :ivar monitored_resources: MonitoredResourcesOperations operations
    :vartype monitored_resources: azure.mgmt.elastic.operations.MonitoredResourcesOperations
    :ivar deployment_info: DeploymentInfoOperations operations
    :vartype deployment_info: azure.mgmt.elastic.operations.DeploymentInfoOperations
    :ivar tag_rules: TagRulesOperations operations
    :vartype tag_rules: azure.mgmt.elastic.operations.TagRulesOperations
    :ivar vm_host: VmHostOperations operations
    :vartype vm_host: azure.mgmt.elastic.operations.VmHostOperations
    :ivar vm_ingestion: VmIngestionOperations operations
    :vartype vm_ingestion: azure.mgmt.elastic.operations.VmIngestionOperations
    :ivar vm_collection: VmCollectionOperations operations
    :vartype vm_collection: azure.mgmt.elastic.operations.VmCollectionOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = MicrosoftElasticConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.monitors = MonitorsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.monitored_resources = MonitoredResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.deployment_info = DeploymentInfoOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.tag_rules = TagRulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.vm_host = VmHostOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.vm_ingestion = VmIngestionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.vm_collection = VmCollectionOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> MicrosoftElastic
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
