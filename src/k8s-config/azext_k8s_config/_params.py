# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands.parameters import (
    get_three_state_flag,
    get_enum_type,
    tags_type
)


def load_arguments(self, _):

    from azure.cli.core.commands.parameters import tags_type
    from azure.cli.core.commands.validators import get_default_location_from_resource_group
    from ._validators import validate_configuration_name, validate_namespace

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
                   arg_type=get_enum_type(['connectedClusters', 'managedClusters']),
                   help='Specify Arc clusters or AKS managed clusters.')

    with self.argument_context('k8s-config flux source') as c:
        c.argument('scope',
                   arg_type=get_enum_type(['namespace', 'cluster']),
                   help="Specify scope of the operator to be 'namespace' or 'cluster'")
        c.argument('namespace',
                   help='Specify namespace to deploy the configuration',
                   validator=validate_namespace)
        c.argument('kind',
                   arg_type=get_enum_type(['git']),
                   options_list=['--kind', '-k'],
                   help='Specify the source kind to reconcile')
        c.argument('url',
                   help='Specify namespace to deploy the configuration')
        c.argument('timeout',
                   help='Specify the source kind to reconcile')
        c.argument('sync_interval',
                   options_list=['--interval', '--sync-interval'],
                   help='Specify the source kind to reconcile')
        c.argument('branch',
                   arg_group="Repo Ref",
                   help='Specify the branch to reconcile the git repository source kind')
        c.argument('tag',
                   arg_group="Repo Ref",
                   help='Specify the branch to reconcile the git repository source kind')
        c.argument('semver',
                   arg_group="Repo Ref",
                   help='Specify the branch to reconcile the git repository source kind')
        c.argument('commit',
                   arg_group="Repo Ref",
                   help='Specify the branch to reconcile the git repository source kind')
        c.argument('auth_ref_override',
                   options_list=['--auth-ref-override', '--auth-ref'],
                   help='Specify the branch to reconcile the git repository source kind')
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

    with self.argument_context('k8s-config flux kustomization') as c:
        c.argument('config_name',
                   help='Specify the name of the configuration to create the kustomization',
                   validator=validate_namespace)
        c.argument('path',
                   help='Specify the name of the configuration to create the kustomization')
        c.argument('dependencies',
                   options_list=['--depends', '--dependencies'],
                   help='Specify the name of the configuration to create the kustomization')
        c.argument('timeout',
                   help='Specify the source kind to reconcile')
        c.argument('sync_interval',
                   options_list=['--interval', '--sync-interval'],
                   help='Specify the source kind to reconcile')
        c.argument('retry_interval',
                   help='Specify the source kind to reconcile')
        c.argument('prune',
                   help='Specify the source kind to reconcile')
        c.argument('force',
                   help='Specify the source kind to reconcile')
        c.argument('validation',
                   arg_type=get_enum_type(['none', 'client', 'server']),
                   help='Specify the source kind to reconcile')
