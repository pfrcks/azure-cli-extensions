# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import base64
from azure.cli.core.azclierror import (
    MutuallyExclusiveArgumentError,
    InvalidArgumentValueError,
    RequiredArgumentMissingError
)
from . import consts


def get_cluster_type(cluster_type):
    if cluster_type.lower() == consts.CONNECTED_CLUSTERS:
        return consts.CONNECTED_RP_NAMESPACE
    # Since cluster_type is an enum of only two values, if not connectedClusters, it will be managedClusters.
    return consts.MANAGED_RP_NAMESPACE


def get_data_from_key_or_file(key, filepath):
    if key != '' and filepath != '':
        raise MutuallyExclusiveArgumentError(
            consts.KEY_AND_FILE_TOGETHER_ERROR,
            consts.KEY_AND_FILE_TOGETHER_HELP)
    data = ''
    if filepath != '':
        data = read_key_file(filepath)
    elif key != '':
        data = key
    return data


def get_protected_settings(ssh_private_key, ssh_private_key_file, https_user, https_key):
    protected_settings = {}
    ssh_private_key_data = get_data_from_key_or_file(ssh_private_key, ssh_private_key_file)

    # Add gitops private key data to protected settings if exists
    # Dry-run all key types to determine if the private key is in a valid format
    if ssh_private_key_data != '':
        protected_settings[consts.SSH_PRIVATE_KEY_KEY] = ssh_private_key_data

    # Check if both httpsUser and httpsKey exist, then add to protected settings
    if https_user != '' and https_key != '':
        protected_settings[consts.HTTPS_USER_KEY] = to_base64(https_user)
        protected_settings[consts.HTTPS_KEY_KEY] = to_base64(https_key)
    elif https_user != '':
        raise RequiredArgumentMissingError(
            consts.HTTPS_USER_WITHOUT_KEY_ERROR,
            consts.HTTPS_USER_WITHOUT_KEY_HELP)
    elif https_key != '':
        raise RequiredArgumentMissingError(
            consts.HTTPS_KEY_WITHOUT_USER_ERROR,
            consts.HTTPS_KEY_WITHOUT_USER_HELP)

    return protected_settings


def read_key_file(path):
    try:
        with open(path, "r") as myfile:  # user passed in filename
            data_list = myfile.readlines()  # keeps newline characters intact
            data_list_len = len(data_list)
            if (data_list_len) <= 0:
                raise Exception("File provided does not contain any data")
            raw_data = ''.join(data_list)
        return to_base64(raw_data)
    except Exception as ex:
        raise InvalidArgumentValueError(
            consts.KEY_FILE_READ_ERROR.format(ex),
            consts.KEY_FILE_READ_HELP) from ex


def parse_dependencies(depends_on):
    depends_on = depends_on.strip()
    if depends_on[0] == '[':
        depends_on = depends_on[1:-1]
    return depends_on.split(',')


def from_base64(base64_str):
    return base64.b64decode(base64_str)


def to_base64(raw_data):
    bytes_data = raw_data.encode('utf-8')
    return base64.b64encode(bytes_data).decode('utf-8')
