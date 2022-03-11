# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_datamigration_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_datamigration.vendored_sdks.datamigration import DataMigrationManagementClient
    return get_mgmt_service_client(cli_ctx,
                                   DataMigrationManagementClient)


def cf_database_migration_sqlmi(cli_ctx, *_):
    return cf_datamigration_cl(cli_ctx).database_migrations_sql_mi


def cf_database_migration_sqlvm(cli_ctx, *_):
    return cf_datamigration_cl(cli_ctx).database_migrations_sql_vm


def cf_sqlmigration_service(cli_ctx, *_):
    return cf_datamigration_cl(cli_ctx).sql_migration_services
