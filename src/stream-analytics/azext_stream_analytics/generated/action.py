# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


# pylint: disable=protected-access

# pylint: disable=no-self-use


import argparse
from collections import defaultdict
from knack.util import CLIError


class AddIdentity(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.identity = action

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'tenant-id':
                d['tenant_id'] = v[0]

            elif kl == 'principal-id':
                d['principal_id'] = v[0]

            elif kl == 'type':
                d['type'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter identity. All possible keys are: tenant-id,'
                    ' principal-id, type'.format(k)
                )

        return d


class AddTransformation(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.transformation = action

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'streaming-units':
                d['streaming_units'] = v[0]

            elif kl == 'valid-streaming-units':
                d['valid_streaming_units'] = v

            elif kl == 'query':
                d['query'] = v[0]

            elif kl == 'name':
                d['name'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter transformation. All possible keys are:'
                    ' streaming-units, valid-streaming-units, query, name'.format(k)
                )

        return d


class AddJobStorageAccount(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.job_storage_account = action

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'authentication-mode':
                d['authentication_mode'] = v[0]

            elif kl == 'account-name':
                d['account_name'] = v[0]

            elif kl == 'account-key':
                d['account_key'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter job-storage-account. All possible keys are:'
                    ' authentication-mode, account-name, account-key'.format(k)
                )

        return d


class AddSku(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.sku = action

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'name':
                d['name'] = v[0]

            elif kl == 'capacity':
                d['capacity'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter sku. All possible keys are: name, capacity'.format(k)
                )

        return d
