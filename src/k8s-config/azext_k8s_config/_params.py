# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-statements

from azure.cli.core.commands.validators import get_default_location_from_resource_group
from azure.cli.core.commands.parameters import (
    get_enum_type,
    tags_type
)
from .validators import validate_configuration_name, validate_namespace
from .action import KustomizationAddAction
from .consts import (
    GIT_CLI_KIND
)


def load_arguments(self, _):
    with self.argument_context('k8s-config') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('name',
                   options_list=['--name', '-n'],
                   help='Name of the configuration',
                   validator=validate_configuration_name)
        c.argument('cluster_name',
                   options_list=['--cluster-name', '-c'],
                   help='Name of the Kubernetes cluster')
        c.argument('cluster_type',
                   options_list=['--cluster-type', '-t'],
                   arg_type=get_enum_type(['connectedClusters', 'managedClusters']),
                   help='Specify Arc connected clusters or AKS managed clusters.')

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
                   arg_type=get_enum_type([GIT_CLI_KIND]),
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
        c.argument('auth_ref_override',
                   options_list=['--auth-ref-override'],
                   arg_group="Auth",
                   help='Local reference to a kubernetes secret in the configuration namespace to use for communication to the source')
        c.argument('kustomization',
                   options_list=['--kustomization', '-k'],
                   action=KustomizationAddAction,
                   help="Define kustomizations to sync sources with parameters ['name', 'path', 'depends_on', 'timeout', 'sync_interval', 'retry_interval', 'prune', 'validation', 'force']",
                   nargs='+')

    # with self.argument_context('k8s-config flux source') as c:
    #     c.argument('scope',
    #                arg_type=get_enum_type(['namespace', 'cluster']),
    #                help="Specify scope of the operator to be 'namespace' or 'cluster'")
    #     c.argument('namespace',
    #                help='Specify namespace to deploy the configuration',
    #                validator=validate_namespace)
    #     c.argument('kind',
    #                arg_type=get_enum_type(['git']),
    #                options_list=['--kind', '-k'],
    #                help='Specify the source kind to reconcile')
    #     c.argument('url',
    #                help='Specify namespace to deploy the configuration')
    #     c.argument('timeout',
    #                help='Specify the source kind to reconcile')
    #     c.argument('sync_interval',
    #                options_list=['--interval', '--sync-interval'],
    #                help='Specify the source kind to reconcile')
    #     c.argument('branch',
    #                arg_group="Repo Ref",
    #                help='Specify the branch to reconcile the git repository source kind')
    #     c.argument('tag',
    #                arg_group="Repo Ref",
    #                help='Specify the branch to reconcile the git repository source kind')
    #     c.argument('semver',
    #                arg_group="Repo Ref",
    #                help='Specify the branch to reconcile the git repository source kind')
    #     c.argument('commit',
    #                arg_group="Repo Ref",
    #                help='Specify the branch to reconcile the git repository source kind')
    #     c.argument('auth_ref_override',
    #                options_list=['--auth-ref-override', '--auth-ref'],
    #                help='Specify the branch to reconcile the git repository source kind')
    #     c.argument('ssh_private_key',
    #                arg_group="Auth",
    #                help='Specify Base64-encoded private ssh key for private repository sync')
    #     c.argument('ssh_private_key_file',
    #                arg_group="Auth",
    #                help='Specify filepath to private ssh key for private repository sync')
    #     c.argument('https_user',
    #                arg_group="Auth",
    #                help='Specify HTTPS username for private repository sync')
    #     c.argument('https_key',
    #                arg_group="Auth",
    #                help='Specify HTTPS token/password for private repository sync')
    #     c.argument('ssh_known_hosts',
    #                arg_group="Auth",
    #                help='Specify Base64-encoded known_hosts contents containing public SSH keys required to access private Git instances')
    #     c.argument('ssh_known_hosts_file',
    #                arg_group="Auth",
    #                help='Specify filepath to known_hosts contents containing public SSH keys required to access private Git instances')

    # with self.argument_context('k8s-config flux kustomization') as c:
    #     c.argument('config_name',
    #                help='Specify the name of the configuration to create the kustomization',
    #                validator=validate_namespace)
    #     c.argument('path',
    #                help='Specify the name of the configuration to create the kustomization')
    #     c.argument('dependencies',
    #                options_list=['--depends', '--dependencies'],
    #                help='Specify the name of the configuration to create the kustomization')
    #     c.argument('timeout',
    #                help='Specify the source kind to reconcile')
    #     c.argument('sync_interval',
    #                options_list=['--interval', '--sync-interval'],
    #                help='Specify the source kind to reconcile')
    #     c.argument('retry_interval',
    #                help='Specify the source kind to reconcile')
    #     c.argument('prune',
    #                help='Specify the source kind to reconcile')
    #     c.argument('force',
    #                help='Specify the source kind to reconcile')
    #     c.argument('validation',
    #                arg_type=get_enum_type(['none', 'client', 'server']),
    #                help='Specify the source kind to reconcile')
