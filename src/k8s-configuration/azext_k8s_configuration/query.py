# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.mgmt.resourcegraph.models import QueryRequest, QueryRequestOptions
from azure.cli.core._profile import Profile


def get_selected_subscription():
    return Profile().get_subscription_id()


class QueryBuilder:
    def __init__(self, resource_type):
        self.query = "KubernetesConfigurationResources"
        self.subs = None
        if resource_type.lower() == "fluxconfigurations":
            self.query += " | where type =~ 'microsoft.kubernetesconfiguration/fluxConfigurations'"

    def with_urls(self, urls):
        self.query = add_filter_to_query(self.query, "properties.gitRepository.url", urls)

    def with_resource_groups(self, resource_groups):
        self.query = add_filter_to_query(self.query, "resourceGroup", resource_groups)
        return self

    def with_cluster_types(self, cluster_types):
        self.query += " | parse id with * '/providers/' * '/' clusterType '/' *"
        self.query = add_filter_to_query(self.query, "clusterType", cluster_types)
        return self

    def with_provisioning_states(self, provisioningStates):
        self.query = add_filter_to_query(
            self.query, "properties['provisioningState']", provisioningStates
        )
        return self

    def with_compliance_states(self, compliance_states):
        self.query = add_filter_to_query(
            self.query, "properties['complianceState']", compliance_states
        )
        return self

    def with_branch(self, branch):
        self.query = add_filter_to_query(
            self.query, "properties.gitRepository.repositoryRef.branch", branch
        )
        return branch

    def with_commit(self, commit):
        self.query = add_contains_filter_to_query(
            self.query, "properties.sourceSyncedCommitId", commit
        )

    def with_subscriptions(self, subscriptions):
        self.subs = subscriptions
        return self

    def build(self):
        request_options = QueryRequestOptions(top=1000, skip=0)
        qr = QueryRequest(
            query=self.query,
            options=request_options,
        )
        if self.subs:
            qr.subscriptions = self.subs
        return qr


def add_filter_to_query(query, key, values):
    if values is not None:
        if not isinstance(values, list):
            values = [values]

        value_filter_string = "','".join(values)
        query += " | where " + key + " in~ ('" + value_filter_string + "')"
    return query

def add_contains_filter_to_query(query, key, value):
    if value is not None:
        query += " | where " + key + " contains '" + value + "'"
    return query