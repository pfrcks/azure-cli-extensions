# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-statements

from azure.cli.core.commands.validators import get_default_location_from_resource_group
from azure.cli.core.commands.parameters import (
    get_enum_type,
    get_three_state_flag,
    tags_type
)
from .validators import validate_configuration_name, validate_extension_name, validate_fluxconfig_name, validate_namespace, validate_operator_instance_name, validate_operator_namespace
from .action import (
    KustomizationAddAction,
    AddConfigurationProtectedSettings,
    AddConfigurationSettings
)
from . import consts


def load_arguments(self, _):
    with self.argument_context('k8s-config') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('cluster_name',
                   options_list=['--cluster-name', '-c'],
                   help='Name of the Kubernetes cluster')
        c.argument('cluster_type',
                   options_list=['--cluster-type', '-t'],
                   arg_type=get_enum_type(['connectedClusters', 'managedClusters']),
                   help='Specify Arc connected clusters or AKS managed clusters.')

    with self.argument_context('k8s-config flux') as c:
        c.argument('name',
                   options_list=['--name', '-n'],
                   help='Name of the flux configuration',
                   validator=validate_fluxconfig_name)

    with self.argument_context('k8s-config flux create') as c:
        c.argument('scope',
                   options_list=['--scope', '-s'],
                   arg_type=get_enum_type(['namespace', 'cluster']),
                   help="Specify scope of the operator to be 'namespace' or 'cluster'")
        c.argument('namespace',
                   help='Namespace to deploy the configuration',
                   options_list=['--namespace', '--ns'],
                   validator=validate_namespace)
        c.argument('kind',
                   arg_type=get_enum_type([consts.GIT]),
                   help='Source kind to reconcile')
        c.argument('url',
                   options_list=['--url', '-u'],
                   help='URL of the source to reconcile')
        c.argument('timeout',
                   help='Maximum time to reconcile the source before timing out')
        c.argument('sync_interval',
                   options_list=['--interval', '--sync-interval'],
                   help='Time between reconciliations of the source on the cluster')
        c.argument('branch',
                   arg_group="Repo Ref",
                   help='Branch to reconcile with the git source')
        c.argument('tag',
                   arg_group="Repo Ref",
                   help='Tag to reconcile with the git source')
        c.argument('semver',
                   arg_group="Repo Ref",
                   help='Semver range to reconcile with the git source')
        c.argument('commit',
                   arg_group="Repo Ref",
                   help='Specific commit to reconcile with the git source')
        c.argument('branch_commit',
                   arg_group="Repo Ref",
                   help="Specific commit and branch to reconcile with the git source")
        c.argument('ssh_private_key',
                   arg_group="Auth",
                   help='Base64-encoded private ssh key for private repository sync')
        c.argument('ssh_private_key_file',
                   arg_group="Auth",
                   help='Filepath to private ssh key for private repository sync')
        c.argument('https_user',
                   arg_group="Auth",
                   help='HTTPS username for private repository sync')
        c.argument('https_key',
                   arg_group="Auth",
                   help='HTTPS token/password for private repository sync')
        c.argument('known_hosts',
                   arg_group="Auth",
                   help='Base64-encoded known_hosts data containing public SSH keys required to access private Git instances')
        c.argument('known_hosts_file',
                   arg_group="Auth",
                   help='Filepath to known_hosts contents containing public SSH keys required to access private Git instances')
        c.argument('local_auth_ref',
                   options_list=['--local-auth-ref'],
                   arg_group="Auth",
                   help='Local reference to a kubernetes secret in the configuration namespace to use for communication to the source')
        c.argument('suspend',
                   help='Suspend the reconciliation of the source and kustomizations associated with this configuration')
        c.argument('kustomization',
                   options_list=['--kustomization', '-k'],
                   action=KustomizationAddAction,
                   help="Define kustomizations to sync sources with parameters ['name', 'path', 'depends_on', 'timeout', 'sync_interval', 'retry_interval', 'prune', 'validation', 'force']",
                   nargs='+')

    with self.argument_context('k8s-config flux delete') as c:
        c.argument('force',
                   help='Specify whether to force delete the flux configuration from the cluster.')

    with self.argument_context('k8s-config extension') as c:
        c.argument('name',
                   options_list=['--name', '-n'],
                   help='Name of the extension',
                   validator=validate_extension_name)

    with self.argument_context('k8s-config extension create') as c:
        c.argument('scope',
                   arg_type=get_enum_type(['cluster', 'namespace']),
                   help='Specify the extension scope.')
        c.argument('auto_upgrade_minor_version',
                   arg_group="Version",
                   options_list=['--auto-upgrade-minor-version', '--auto-upgrade'],
                   arg_type=get_three_state_flag(),
                   help='Automatically upgrade minor version of the extension instance.')
        c.argument('version',
                   arg_group="Version",
                   help='Specify the version to install for the extension instance if'
                   ' --auto-upgrade-minor-version is not enabled.')
        c.argument('release_train',
                   arg_group="Version",
                   help='Specify the release train for the extension type.')
        c.argument('configuration_settings',
                   arg_group="Configuration",
                   options_list=['--configuration-settings', '--config'],
                   action=AddConfigurationSettings,
                   nargs='+',
                   help='Configuration Settings as key=value pair.  Repeat parameter for each setting')
        c.argument('configuration_protected_settings',
                   arg_group="Configuration",
                   options_list=['--configuration-protected-settings', '--config-protected'],
                   action=AddConfigurationProtectedSettings,
                   nargs='+',
                   help='Configuration Protected Settings as key=value pair.  Repeat parameter for each setting')
        c.argument('configuration_settings_file',
                   arg_group="Configuration",
                   options_list=['--configuration-settings-file', '--config-file'],
                   help='JSON file path for configuration-settings')
        c.argument('configuration_protected_settings_file',
                   arg_group="Configuration",
                   options_list=['--configuration-protected-settings-file', '--config-protected-file'],
                   help='JSON file path for configuration-protected-settings')
        c.argument('release_namespace',
                   help='Specify the namespace to install the extension release.')
        c.argument('target_namespace',
                   help='Specify the target namespace to install to for the extension instance. This'
                   ' parameter is required if extension scope is set to \'namespace\'')

    with self.argument_context('k8s-config extension delete') as c:
        c.argument('force',
                   help='Specify whether to force delete the extension from the cluster.')

    with self.argument_context('k8s-config fluxv1') as c:
        c.argument('name',
                   options_list=['--name', '-n'],
                   help='Name of the configuration',
                   validator=validate_configuration_name)

    with self.argument_context('k8s-config fluxv1 create') as c:
        c.argument('repository_url',
                   options_list=['--repository-url', '-u'],
                   help='Url of the source control repository')
        c.argument('scope',
                   arg_type=get_enum_type(['namespace', 'cluster']),
                   help='''Specify scope of the operator to be 'namespace' or 'cluster' ''')
        c.argument('enable_helm_operator',
                   arg_group="Helm Operator",
                   arg_type=get_three_state_flag(),
                   options_list=['--enable-helm-operator', '--enable-hop'],
                   help='Enable support for Helm chart deployments')
        c.argument('helm_operator_params',
                   arg_group="Helm Operator",
                   options_list=['--helm-operator-params', '--hop-params'],
                   help='Chart values for the Helm Operator (if enabled)')
        c.argument('helm_operator_chart_version',
                   arg_group="Helm Operator",
                   options_list=['--helm-operator-chart-version', '--hop-chart-version'],
                   help='Chart version of the Helm Operator (if enabled)')
        c.argument('operator_params',
                   arg_group="Operator",
                   help='Parameters for the Operator')
        c.argument('operator_instance_name',
                   arg_group="Operator",
                   help='Instance name of the Operator',
                   validator=validate_operator_instance_name)
        c.argument('operator_namespace',
                   arg_group="Operator",
                   help='Namespace in which to install the Operator',
                   validator=validate_operator_namespace)
        c.argument('operator_type',
                   arg_group="Operator",
                   help='''Type of the operator. Valid value is 'flux' ''')
        c.argument('ssh_private_key',
                   arg_group="Auth",
                   help='Specify Base64-encoded private ssh key for private repository sync')
        c.argument('ssh_private_key_file',
                   arg_group="Auth",
                   help='Specify filepath to private ssh key for private repository sync')
        c.argument('https_user',
                   arg_group="Auth",
                   help='Specify HTTPS username for private repository sync')
        c.argument('https_key',
                   arg_group="Auth",
                   help='Specify HTTPS token/password for private repository sync')
        c.argument('ssh_known_hosts',
                   arg_group="Auth",
                   help='Specify Base64-encoded known_hosts contents containing public SSH keys required to access private Git instances')
        c.argument('ssh_known_hosts_file',
                   arg_group="Auth",
                   help='Specify filepath to known_hosts contents containing public SSH keys required to access private Git instances')

    with self.argument_context('k8s-config flux source') as c:
        c.argument('scope',
                   options_list=['--scope', '-s'],
                   arg_type=get_enum_type(['namespace', 'cluster']),
                   help="Specify scope of the operator to be 'namespace' or 'cluster'")
        c.argument('namespace',
                   help='Namespace to deploy the configuration',
                   options_list=['--namespace', '--ns'],
                   validator=validate_namespace)
        c.argument('kind',
                   arg_type=get_enum_type([consts.GIT]),
                   help='Source kind to reconcile')
        c.argument('url',
                   options_list=['--url', '-u'],
                   help='URL of the source to reconcile')
        c.argument('timeout',
                   help='Maximum time to reconcile the source before timing out')
        c.argument('sync_interval',
                   options_list=['--interval', '--sync-interval'],
                   help='Time between reconciliations of the source on the cluster')
        c.argument('branch',
                   arg_group="Repo Ref",
                   help='Branch to reconcile with the git source')
        c.argument('tag',
                   arg_group="Repo Ref",
                   help='Tag to reconcile with the git source')
        c.argument('semver',
                   arg_group="Repo Ref",
                   help='Semver range to reconcile with the git source')
        c.argument('commit',
                   arg_group="Repo Ref",
                   help='Specific commit to reconcile with the git source')
        c.argument('ssh_private_key',
                   arg_group="Auth",
                   help='Base64-encoded private ssh key for private repository sync')
        c.argument('ssh_private_key_file',
                   arg_group="Auth",
                   help='Filepath to private ssh key for private repository sync')
        c.argument('https_user',
                   arg_group="Auth",
                   help='HTTPS username for private repository sync')
        c.argument('https_key',
                   arg_group="Auth",
                   help='HTTPS token/password for private repository sync')
        c.argument('known_hosts',
                   arg_group="Auth",
                   help='Base64-encoded known_hosts data containing public SSH keys required to access private Git instances')
        c.argument('known_hosts_file',
                   arg_group="Auth",
                   help='Filepath to known_hosts contents containing public SSH keys required to access private Git instances')
        c.argument('local_auth_ref',
                   options_list=['--local-auth-ref'],
                   arg_group="Auth",
                   help='Local reference to a kubernetes secret in the configuration namespace to use for communication to the source')

    with self.argument_context('k8s-config flux kustomization') as c:
        c.argument('kustomization_name',
                   help='Specify the name of the kustomization to add to the configuration')
        c.argument('path',
                   help='Specify the path in the source that the kustomization should apply')
        c.argument('dependencies',
                   options_list=['--depends', '--dependencies'],
                   help='Specify the names of kustomization dependencies')
        c.argument('timeout',
                   help='Maximum time to reconcile the kustomization before timing out')
        c.argument('sync_interval',
                   options_list=['--interval', '--sync-interval'],
                   help='Time between reconciliations of the kustomization on the cluster')
        c.argument('retry_interval',
                   help='Time between reconciliations of the kustomization on the cluster on failures, defaults to --sync-interval')
        c.argument('prune',
                   help='Whether to garbage collect resources deployed by the kustomization on the cluster')
        c.argument('force',
                   help='Whether to re-create resources that cannot be updated on the cluster (i.e. jobs)')
        c.argument('validation',
                   arg_type=get_enum_type(['none', 'client', 'server']),
                   help='Specify whether to dry-run manifests at the client or at the apiserver level before applying them to the cluster.')
