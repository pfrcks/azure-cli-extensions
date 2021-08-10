# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from collections import OrderedDict


def sourcecontrol_list_table_format(results):
    return [__get_sourcecontrolconfig_table_row(result) for result in results]


def sourcecontrol_show_table_format(result):
    return __get_sourcecontrolconfig_table_row(result)


def __get_sourcecontrolconfig_table_row(result):
    return OrderedDict([
        ('name', result['name']),
        ('repositoryUrl', result['repositoryUrl']),
        ('operatorName', result['operatorInstanceName']),
        ('operatorNamespace', result['operatorNamespace']),
        ('scope', result['operatorScope']),
        ('provisioningState', result['provisioningState'])
    ])


def extension_list_table_format(results):
    return [__get_extension_table_row(result) for result in results]


def extension_show_table_format(result):
    return __get_extension_table_row(result)


def __get_extension_table_row(result):
    return OrderedDict([
        ('name', result['name']),
        ('extensionType', result['extensionType']),
        ('version', result['version']),
        ('installState', result['installState']),
        ('lastModifiedTime', result['lastModifiedTime'])
    ])


def fluxconfig_list_table_format(results):
    return [__get_fluxconfig_table_row(result) for result in results]


def fluxconfig_show_table_format(result):
    return __get_fluxconfig_table_row(result)


def __get_fluxconfig_table_row(result):
    return OrderedDict([
        ('name', result['name']),
        ('provisioningState', result['provisioningState']),
        ('syncState', result['syncState']),
        ('namespace', result['namespace']),
        ('scope', result['scope']),
        ('lastSyncedTime', result['lastSyncedTime']),
    ])