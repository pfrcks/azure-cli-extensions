# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


from .. import try_manual

MACHINE_NAME = 'sdkTestVM'
RESOURCE_GROUP = 'az-sdk-test'
LOCATION = 'eastus2euap'
EXTENSION_NAME = 'CustomScriptExtension'
SCOPE_NAME = ''
PRIVATE_ENDPOINT_NAME = ''


# EXAMPLE: /Machines/get/Get Machine
@try_manual
def step_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az connectedmachine show '
             f'--name "{MACHINE_NAME}" '
             f'--resource-group "{RESOURCE_GROUP}"',
             checks=checks)


# EXAMPLE: /Machines/get/List Machines by resource group
@try_manual
def step_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az connectedmachine list '
             f'--resource-group "{RESOURCE_GROUP}"',
             checks=checks)


# EXAMPLE: /MachineExtensions/put/Create or Update a Machine Extension
@try_manual
def step_extension_create(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az connectedmachine extension create '
             '--name "CustomScriptExtension" '
             '--location "eastus2euap" '
             '--enable-auto-upgrade true '
             '--type "CustomScriptExtension" '
             '--publisher "Microsoft.Compute" '
             '--settings "{{\\"commandToExecute\\":\\"powershell.exe -c \\\\\\"Get-Process | Where-Object {{{{ $_.CPU '
             '-gt 10000 }}}}\\\\\\"\\"}}" '
             '--type-handler-version "1.10.10" '
             f'--machine-name "{MACHINE_NAME}" '
             f'--resource-group "{RESOURCE_GROUP}"',
             checks=checks)


# EXAMPLE: /MachineExtensions/get/GET all Machine Extensions
@try_manual
def step_extension_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az connectedmachine extension list '
             f'--machine-name "{MACHINE_NAME}" '
             f'--resource-group "{RESOURCE_GROUP}"',
             checks=checks)


# EXAMPLE: /MachineExtensions/get/GET Machine Extension
@try_manual
def step_extension_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az connectedmachine extension show '
             f'--name "CustomScriptExtension" '
             f'--machine-name "{MACHINE_NAME}" '
             f'--resource-group "{RESOURCE_GROUP}"',
             checks=checks)


# EXAMPLE: /connectedmachine/post/Upgrade Machine Extensions
@try_manual
def step_upgrade_extension(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az connectedmachine upgrade-extension '
             '--extension-targets "{{\\"Microsoft.Compute.CustomScriptExtension\\":{{\\"targetVersion\\":\\"1.10.12\\"}}}}" '
             f'--machine-name "{MACHINE_NAME}" '
             f'--resource-group "{RESOURCE_GROUP}"',
             checks=checks)


# EXAMPLE: /MachineExtensions/patch/Create or Update a Machine Extension
@try_manual
def step_extension_update(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az connectedmachine extension update '
             f'--name "{EXTENSION_NAME}" '
             '--enable-auto-upgrade false '
             '--settings "{{\\"commandToExecute\\":\\"hostname\\"}}" '
             f'--machine-name "{MACHINE_NAME}" '
             f'--resource-group "{RESOURCE_GROUP}"',
             checks=checks) 


# EXAMPLE: /MachineExtensions/delete/Delete a Machine Extension
@try_manual
def step_extension_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az connectedmachine extension delete -y '
             f'--name "{EXTENSION_NAME}" '
             f'--machine-name "{MACHINE_NAME}" '
             f'--resource-group "{RESOURCE_GROUP}"',
             checks=checks)


# EXAMPLE: /Machines/delete/Delete a Machine
@try_manual
def step_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az connectedmachine delete -y '
             f'--name "{MACHINE_NAME}" '
             f'--resource-group "{RESOURCE_GROUP}"',
             checks=checks)


# EXAMPLE: /PrivateEndpointConnections/put/Approve or reject a private endpoint connection with a given name.
@try_manual
def step_private_endpoint_connection_update(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az connectedmachine private-endpoint-connection update '
             '--connection-state description="Approved by johndoe@contoso.com" status="Approved" '
             f'--name "{PRIVATE_ENDPOINT_NAME}" '
             f'--resource-group "{RESOURCE_GROUP}" '
             f'--scope-name "{SCOPE_NAME}"',
             checks=[])


# EXAMPLE: /PrivateEndpointConnections/get/Gets list of private endpoint connections on a private link scope.
@try_manual
def step_private_endpoint_connection_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az connectedmachine private-endpoint-connection list '
             f'--resource-group "{RESOURCE_GROUP}" '
             f'--scope-name "{SCOPE_NAME}"',
             checks=checks)


# EXAMPLE: /PrivateEndpointConnections/get/Gets private endpoint connection.
@try_manual
def step_private_endpoint_connection_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az connectedmachine private-endpoint-connection show '
             f'--name "{PRIVATE_ENDPOINT_NAME}" '
             f'--resource-group "{RESOURCE_GROUP}" '
             f'--scope-name "{SCOPE_NAME}"',
             checks=checks)


# EXAMPLE: /PrivateEndpointConnections/delete/Deletes a private endpoint connection with a given name.
@try_manual
def step_private_endpoint_connection_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az connectedmachine private-endpoint-connection delete -y '
             f'--name "{PRIVATE_ENDPOINT_NAME}" '
             f'--resource-group "{RESOURCE_GROUP}" '
             f'--scope-name "{SCOPE_NAME}"',
             checks=checks)


# EXAMPLE: /PrivateLinkResources/get/Gets private endpoint connection.
@try_manual
def step_private_link_resource_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az connectedmachine private-link-resource list '
             f'--resource-group "{RESOURCE_GROUP}" '
             f'--scope-name "{SCOPE_NAME}"',
             checks=checks)


# EXAMPLE: /PrivateLinkScopes/put/PrivateLinkScopeCreate
@try_manual
def step_private_link_scope_create(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az connectedmachine private-link-scope create '
             f'--location "{LOCATION}" '
             f'--resource-group "{RESOURCE_GROUP}" '
             f'--scope-name "{SCOPE_NAME}"',
             checks=checks)


# EXAMPLE: /PrivateLinkScopes/put/PrivateLinkScopeUpdate
@try_manual
def step_private_link_scope_update(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az connectedmachine private-link-scope update '
             f'--location "{LOCATION}" '
             '--tags Tag1="Value1" '
             '--public-network-access Enabled '
             f'--resource-group "{RESOURCE_GROUP}" '
             f'--scope-name "{SCOPE_NAME}"',
             checks=checks)


# EXAMPLE: /PrivateLinkScopes/get/PrivateLinkScopeGet
@try_manual
def step_private_link_scope_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az connectedmachine private-link-scope show '
             f'--resource-group "{RESOURCE_GROUP}" '
             f'--scope-name "{SCOPE_NAME}"',
             checks=checks)


# EXAMPLE: /PrivateLinkScopes/get/PrivateLinkScopeListByResourceGroup
@try_manual
def step_private_link_scope_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az connectedmachine private-link-scope list '
             f'--resource-group "{RESOURCE_GROUP}"',
             checks=checks)


# EXAMPLE: /PrivateLinkScopes/patch/PrivateLinkScopeUpdateTagsOnly
@try_manual
def step_private_link_scope_update_tag(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az connectedmachine private-link-scope update-tag '
             '--tags Tag1="Value1" Tag2="Value2" '
             f'--resource-group "{RESOURCE_GROUP}" '
             f'--scope-name "{SCOPE_NAME}"',
             checks=checks)


# EXAMPLE: /PrivateLinkScopes/delete/PrivateLinkScopesDelete
@try_manual
def step_private_link_scope_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az connectedmachine private-link-scope delete -y '
             f'--resource-group "{RESOURCE_GROUP}" '
             f'--scope-name "{SCOPE_NAME}"',
             checks=checks)
