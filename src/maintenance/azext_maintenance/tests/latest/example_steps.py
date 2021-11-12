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


# EXAMPLE: /ApplyUpdates/put/ApplyUpdates_CreateOrUpdate
@try_manual
def step_applyupdate_create(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az maintenance applyupdate create '
             '--provider-name "Microsoft.Compute" '
             '--resource-group "{rg}" '
             '--resource-name "smdtest1" '
             '--resource-type "virtualMachineScaleSets"',
             checks=checks)


# EXAMPLE: /ApplyUpdates/put/ApplyUpdates_CreateOrUpdateParent
@try_manual
def step_applyupdate_create_or_update_parent(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az maintenance applyupdate create-or-update-parent '
             '--provider-name "Microsoft.Compute" '
             '--resource-group "{rg}" '
             '--resource-name "smdvm1" '
             '--resource-parent-name "smdtest1" '
             '--resource-parent-type "virtualMachineScaleSets" '
             '--resource-type "virtualMachines"',
             checks=checks)


# EXAMPLE: /ApplyUpdates/get/ApplyUpdates_Get
@try_manual
def step_applyupdate_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az maintenance applyupdate show '
             '--name "{myApplyUpdate}" '
             '--provider-name "Microsoft.Compute" '
             '--resource-group "{rg}" '
             '--resource-name "smdtest1" '
             '--resource-type "virtualMachineScaleSets"',
             checks=checks)


# EXAMPLE: /ApplyUpdates/get/ApplyUpdates_GetParent
@try_manual
def step_applyupdate_show_parent(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az maintenance applyupdate show-parent '
             '--name "{myApplyUpdate}" '
             '--provider-name "Microsoft.Compute" '
             '--resource-group "{rg}" '
             '--resource-name "smdvm1" '
             '--resource-parent-name "smdtest1" '
             '--resource-parent-type "virtualMachineScaleSets" '
             '--resource-type "virtualMachines"',
             checks=checks)


# EXAMPLE: /ApplyUpdates/get/ApplyUpdates_List
@try_manual
def step_applyupdate_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az maintenance applyupdate list',
             checks=checks)


# EXAMPLE: /MaintenanceConfigurations/put/MaintenanceConfigurations_CreateOrUpdateForResource
@try_manual
def step_configuration_create(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az maintenance configuration create '
             '--location "eastus2euap" '
             '--maintenance-scope "OSImage" '
             '--maintenance-window-duration "05:00" '
             '--maintenance-window-expiration-date-time "9999-12-31 00:00" '
             '--maintenance-window-recur-every "Day" '
             '--maintenance-window-start-date-time "2020-04-30 08:00" '
             '--maintenance-window-time-zone "Pacific Standard Time" '
             '--namespace "Microsoft.Maintenance" '
             '--visibility "Custom" '
             '--resource-group "{rg}" '
             '--resource-name "{myMaintenanceConfiguration}"',
             checks=checks)


# EXAMPLE: /MaintenanceConfigurations/get/MaintenanceConfigurations_GetForResource
@try_manual
def step_configuration_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az maintenance configuration show '
             '--resource-group "{rg}" '
             '--resource-name "{myMaintenanceConfiguration}"',
             checks=checks)


# EXAMPLE: /MaintenanceConfigurations/get/MaintenanceConfigurations_GetForResource_GuestOSPatchLinux
@try_manual
def step_configuration_show2(test, checks=None):
    return step_configuration_show(test, checks)


# EXAMPLE: /MaintenanceConfigurations/get/MaintenanceConfigurations_GetForResource_GuestOSPatchWindows
@try_manual
def step_configuration_show3(test, checks=None):
    return step_configuration_show(test, checks)


# EXAMPLE: /MaintenanceConfigurations/get/MaintenanceConfigurations_List
@try_manual
def step_configuration_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az maintenance configuration list',
             checks=checks)


# EXAMPLE: /MaintenanceConfigurations/patch/MaintenanceConfigurations_UpdateForResource
@try_manual
def step_configuration_update(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az maintenance configuration update '
             '--location "eastus2euap" '
             '--maintenance-scope "OSImage" '
             '--maintenance-window-duration "05:00" '
             '--maintenance-window-expiration-date-time "9999-12-31 00:00" '
             '--maintenance-window-recur-every "Month Third Sunday" '
             '--maintenance-window-start-date-time "2020-04-30 08:00" '
             '--maintenance-window-time-zone "Pacific Standard Time" '
             '--namespace "Microsoft.Maintenance" '
             '--visibility "Custom" '
             '--resource-group "{rg}" '
             '--resource-name "{myMaintenanceConfiguration}"',
             checks=checks)


# EXAMPLE: /ConfigurationAssignments/put/ConfigurationAssignments_CreateOrUpdate
@try_manual
def step_assignment_create(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az maintenance assignment create '
             '--maintenance-configuration-id "/subscriptions/{subscription_id}/resourcegroups/{rg}/providers/Microsoft.'
             'Maintenance/maintenanceConfigurations/{myMaintenanceConfiguration}" '
             '--name "{myConfigurationAssignment}" '
             '--provider-name "Microsoft.Compute" '
             '--resource-group "{rg}" '
             '--resource-name "smdtest1" '
             '--resource-type "virtualMachineScaleSets"',
             checks=checks)


# EXAMPLE: /ConfigurationAssignments/put/ConfigurationAssignments_CreateOrUpdateParent
@try_manual
def step_assignment_create_or_update_parent(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az maintenance assignment create-or-update-parent '
             '--maintenance-configuration-id "/subscriptions/{subscription_id}/resourcegroups/{rg}/providers/Microsoft.'
             'Maintenance/maintenanceConfigurations/{myMaintenanceConfiguration2}" '
             '--name "{myConfigurationAssignment2}" '
             '--provider-name "Microsoft.Compute" '
             '--resource-group "{rg}" '
             '--resource-name "smdvm1" '
             '--resource-parent-name "smdtest1" '
             '--resource-parent-type "virtualMachineScaleSets" '
             '--resource-type "virtualMachines"',
             checks=checks)


# EXAMPLE: /ConfigurationAssignments/get/ConfigurationAssignments_Get
@try_manual
def step_assignment_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az maintenance assignment show '
             '--name "{myConfigurationAssignment}" '
             '--provider-name "Microsoft.Compute" '
             '--resource-group "{rg}" '
             '--resource-name "smdtest1" '
             '--resource-type "virtualMachineScaleSets"',
             checks=checks)


# EXAMPLE: /ConfigurationAssignments/get/ConfigurationAssignments_GetParent
@try_manual
def step_assignment_show_parent(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az maintenance assignment show-parent '
             '--name "{myConfigurationAssignment2}" '
             '--provider-name "Microsoft.Compute" '
             '--resource-group "{rg}" '
             '--resource-name "smdvm1" '
             '--resource-parent-name "smdtest1" '
             '--resource-parent-type "virtualMachineScaleSets" '
             '--resource-type "virtualMachines"',
             checks=checks)


# EXAMPLE: /ConfigurationAssignments/get/ConfigurationAssignments_List
@try_manual
def step_assignment_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az maintenance assignment list '
             '--provider-name "Microsoft.Compute" '
             '--resource-group "{rg}" '
             '--resource-name "smdtest1" '
             '--resource-type "virtualMachineScaleSets"',
             checks=checks)


# EXAMPLE: /ConfigurationAssignments/get/ConfigurationAssignments_ListParent
@try_manual
def step_assignment_list_parent(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az maintenance assignment list-parent '
             '--provider-name "Microsoft.Compute" '
             '--resource-group "{rg}" '
             '--resource-name "smdtestvm1" '
             '--resource-parent-name "smdtest1" '
             '--resource-parent-type "virtualMachineScaleSets" '
             '--resource-type "virtualMachines"',
             checks=checks)


# EXAMPLE: /ConfigurationAssignments/delete/ConfigurationAssignments_Delete
@try_manual
def step_assignment_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az maintenance assignment delete -y '
             '--name "{myConfigurationAssignment}" '
             '--provider-name "Microsoft.Compute" '
             '--resource-group "{rg}" '
             '--resource-name "smdtest1" '
             '--resource-type "virtualMachineScaleSets"',
             checks=checks)


# EXAMPLE: /ConfigurationAssignments/delete/ConfigurationAssignments_DeleteParent
@try_manual
def step_assignment_delete_parent(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az maintenance assignment delete-parent '
             '--name "{myConfigurationAssignment}" '
             '--provider-name "Microsoft.Compute" '
             '--resource-group "{rg}" '
             '--resource-name "smdvm1" '
             '--resource-parent-name "smdtest1" '
             '--resource-parent-type "virtualMachineScaleSets" '
             '--resource-type "virtualMachines"',
             checks=checks)


# EXAMPLE: /MaintenanceConfigurations/delete/MaintenanceConfigurations_DeleteForResource
@try_manual
def step_configuration_delete(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az maintenance configuration delete -y '
             '--resource-group "{rg}" '
             '--resource-name "example1"',
             checks=checks)


# EXAMPLE: /PublicMaintenanceConfigurations/get/PublicMaintenanceConfigurations_GetForResource
@try_manual
def step_public_configuration_show(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az maintenance public-configuration show '
             '--resource-name "{myMaintenanceConfiguration}"',
             checks=checks)


# EXAMPLE: /PublicMaintenanceConfigurations/get/PublicMaintenanceConfigurations_List
@try_manual
def step_public_configuration_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az maintenance public-configuration list',
             checks=checks)


# EXAMPLE: /Updates/get/Updates_List
@try_manual
def step_update_list(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az maintenance update list '
             '--provider-name "Microsoft.Compute" '
             '--resource-group "{rg}" '
             '--resource-name "smdtest1" '
             '--resource-type "virtualMachineScaleSets"',
             checks=checks)


# EXAMPLE: /Updates/get/Updates_ListParent
@try_manual
def step_update_list_parent(test, checks=None):
    if checks is None:
        checks = []
    test.cmd('az maintenance update list-parent '
             '--provider-name "Microsoft.Compute" '
             '--resource-group "{rg}" '
             '--resource-name "1" '
             '--resource-parent-name "smdtest1" '
             '--resource-parent-type "virtualMachineScaleSets" '
             '--resource-type "virtualMachines"',
             checks=checks)
