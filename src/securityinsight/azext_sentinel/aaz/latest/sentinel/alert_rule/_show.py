# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "sentinel alert-rule show",
    is_experimental=True,
)
class Show(AAZCommand):
    """Get the alert rule.
    """

    _aaz_info = {
        "version": "2022-06-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.operationalinsights/workspaces/{}/providers/microsoft.securityinsights/alertrules/{}", "2022-06-01-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.rule_name = AAZStrArg(
            options=["-n", "--name", "--rule-name"],
            help="Name of alert rule.",
            required=True,
            is_experimental=True,
            id_part="child_name_1",
        )
        _args_schema.workspace_name = AAZStrArg(
            options=["-w", "--workspace-name"],
            help="The name of the workspace.",
            required=True,
            is_experimental=True,
            id_part="name",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.AlertRulesGet(ctx=self.ctx)()

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class AlertRulesGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/providers/Microsoft.SecurityInsights/alertRules/{ruleId}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "ruleId", self.ctx.args.rule_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "workspaceName", self.ctx.args.workspace_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-06-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.etag = AAZStrType()
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.kind = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
                flags={"read_only": True},
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
                flags={"read_only": True},
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
                flags={"read_only": True},
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
                flags={"read_only": True},
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
                flags={"read_only": True},
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
                flags={"read_only": True},
            )

            disc_fusion = cls._schema_on_200.discriminate_by("kind", "Fusion")
            disc_fusion.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.discriminate_by("kind", "Fusion").properties
            properties.alert_rule_template_name = AAZStrType(
                serialized_name="alertRuleTemplateName",
                flags={"required": True},
            )
            properties.description = AAZStrType(
                flags={"read_only": True},
            )
            properties.display_name = AAZStrType(
                serialized_name="displayName",
                flags={"read_only": True},
            )
            properties.enabled = AAZBoolType(
                flags={"required": True},
            )
            properties.last_modified_utc = AAZStrType(
                serialized_name="lastModifiedUtc",
                flags={"read_only": True},
            )
            properties.scenario_exclusion_patterns = AAZListType(
                serialized_name="scenarioExclusionPatterns",
            )
            properties.severity = AAZStrType(
                flags={"read_only": True},
            )
            properties.source_settings = AAZListType(
                serialized_name="sourceSettings",
            )
            properties.tactics = AAZListType(
                flags={"read_only": True},
            )
            properties.techniques = AAZListType(
                flags={"read_only": True},
            )

            scenario_exclusion_patterns = cls._schema_on_200.discriminate_by("kind", "Fusion").properties.scenario_exclusion_patterns
            scenario_exclusion_patterns.Element = AAZObjectType()

            _element = cls._schema_on_200.discriminate_by("kind", "Fusion").properties.scenario_exclusion_patterns.Element
            _element.date_added_in_utc = AAZStrType(
                serialized_name="dateAddedInUTC",
                flags={"required": True},
            )
            _element.exclusion_pattern = AAZStrType(
                serialized_name="exclusionPattern",
                flags={"required": True},
            )

            source_settings = cls._schema_on_200.discriminate_by("kind", "Fusion").properties.source_settings
            source_settings.Element = AAZObjectType()

            _element = cls._schema_on_200.discriminate_by("kind", "Fusion").properties.source_settings.Element
            _element.enabled = AAZBoolType(
                flags={"required": True},
            )
            _element.source_name = AAZStrType(
                serialized_name="sourceName",
                flags={"required": True},
            )
            _element.source_sub_types = AAZListType(
                serialized_name="sourceSubTypes",
            )

            source_sub_types = cls._schema_on_200.discriminate_by("kind", "Fusion").properties.source_settings.Element.source_sub_types
            source_sub_types.Element = AAZObjectType()

            _element = cls._schema_on_200.discriminate_by("kind", "Fusion").properties.source_settings.Element.source_sub_types.Element
            _element.enabled = AAZBoolType(
                flags={"required": True},
            )
            _element.severity_filters = AAZObjectType(
                serialized_name="severityFilters",
                flags={"required": True},
            )
            _element.source_sub_type_display_name = AAZStrType(
                serialized_name="sourceSubTypeDisplayName",
                flags={"read_only": True},
            )
            _element.source_sub_type_name = AAZStrType(
                serialized_name="sourceSubTypeName",
                flags={"required": True},
            )

            severity_filters = cls._schema_on_200.discriminate_by("kind", "Fusion").properties.source_settings.Element.source_sub_types.Element.severity_filters
            severity_filters.filters = AAZListType()
            severity_filters.is_supported = AAZBoolType(
                serialized_name="isSupported",
                flags={"read_only": True},
            )

            filters = cls._schema_on_200.discriminate_by("kind", "Fusion").properties.source_settings.Element.source_sub_types.Element.severity_filters.filters
            filters.Element = AAZObjectType()

            _element = cls._schema_on_200.discriminate_by("kind", "Fusion").properties.source_settings.Element.source_sub_types.Element.severity_filters.filters.Element
            _element.enabled = AAZBoolType(
                flags={"required": True},
            )
            _element.severity = AAZStrType(
                flags={"required": True},
            )

            tactics = cls._schema_on_200.discriminate_by("kind", "Fusion").properties.tactics
            tactics.Element = AAZStrType(
                flags={"read_only": True},
            )

            techniques = cls._schema_on_200.discriminate_by("kind", "Fusion").properties.techniques
            techniques.Element = AAZStrType(
                flags={"read_only": True},
            )

            disc_ml_behavior_analytics = cls._schema_on_200.discriminate_by("kind", "MLBehaviorAnalytics")
            disc_ml_behavior_analytics.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.discriminate_by("kind", "MLBehaviorAnalytics").properties
            properties.alert_rule_template_name = AAZStrType(
                serialized_name="alertRuleTemplateName",
                flags={"required": True},
            )
            properties.description = AAZStrType(
                flags={"read_only": True},
            )
            properties.display_name = AAZStrType(
                serialized_name="displayName",
                flags={"read_only": True},
            )
            properties.enabled = AAZBoolType(
                flags={"required": True},
            )
            properties.last_modified_utc = AAZStrType(
                serialized_name="lastModifiedUtc",
                flags={"read_only": True},
            )
            properties.severity = AAZStrType(
                flags={"read_only": True},
            )
            properties.tactics = AAZListType(
                flags={"read_only": True},
            )
            properties.techniques = AAZListType(
                flags={"read_only": True},
            )

            tactics = cls._schema_on_200.discriminate_by("kind", "MLBehaviorAnalytics").properties.tactics
            tactics.Element = AAZStrType(
                flags={"read_only": True},
            )

            techniques = cls._schema_on_200.discriminate_by("kind", "MLBehaviorAnalytics").properties.techniques
            techniques.Element = AAZStrType(
                flags={"read_only": True},
            )

            disc_microsoft_security_incident_creation = cls._schema_on_200.discriminate_by("kind", "MicrosoftSecurityIncidentCreation")
            disc_microsoft_security_incident_creation.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.discriminate_by("kind", "MicrosoftSecurityIncidentCreation").properties
            properties.alert_rule_template_name = AAZStrType(
                serialized_name="alertRuleTemplateName",
            )
            properties.description = AAZStrType()
            properties.display_name = AAZStrType(
                serialized_name="displayName",
                flags={"required": True},
            )
            properties.display_names_exclude_filter = AAZListType(
                serialized_name="displayNamesExcludeFilter",
            )
            properties.display_names_filter = AAZListType(
                serialized_name="displayNamesFilter",
            )
            properties.enabled = AAZBoolType(
                flags={"required": True},
            )
            properties.last_modified_utc = AAZStrType(
                serialized_name="lastModifiedUtc",
                flags={"read_only": True},
            )
            properties.product_filter = AAZStrType(
                serialized_name="productFilter",
                flags={"required": True},
            )
            properties.severities_filter = AAZListType(
                serialized_name="severitiesFilter",
            )

            display_names_exclude_filter = cls._schema_on_200.discriminate_by("kind", "MicrosoftSecurityIncidentCreation").properties.display_names_exclude_filter
            display_names_exclude_filter.Element = AAZStrType()

            display_names_filter = cls._schema_on_200.discriminate_by("kind", "MicrosoftSecurityIncidentCreation").properties.display_names_filter
            display_names_filter.Element = AAZStrType()

            severities_filter = cls._schema_on_200.discriminate_by("kind", "MicrosoftSecurityIncidentCreation").properties.severities_filter
            severities_filter.Element = AAZStrType()

            disc_nrt = cls._schema_on_200.discriminate_by("kind", "NRT")
            disc_nrt.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.discriminate_by("kind", "NRT").properties
            properties.alert_details_override = AAZObjectType(
                serialized_name="alertDetailsOverride",
            )
            _build_schema_alert_details_override_read(properties.alert_details_override)
            properties.alert_rule_template_name = AAZStrType(
                serialized_name="alertRuleTemplateName",
            )
            properties.custom_details = AAZDictType(
                serialized_name="customDetails",
            )
            properties.description = AAZStrType()
            properties.display_name = AAZStrType(
                serialized_name="displayName",
                flags={"required": True},
            )
            properties.enabled = AAZBoolType(
                flags={"required": True},
            )
            properties.entity_mappings = AAZListType(
                serialized_name="entityMappings",
            )
            _build_schema_entity_mappings_read(properties.entity_mappings)
            properties.incident_configuration = AAZObjectType(
                serialized_name="incidentConfiguration",
            )
            _build_schema_incident_configuration_read(properties.incident_configuration)
            properties.last_modified_utc = AAZStrType(
                serialized_name="lastModifiedUtc",
                flags={"read_only": True},
            )
            properties.query = AAZStrType(
                flags={"required": True},
            )
            properties.severity = AAZStrType(
                flags={"required": True},
            )
            properties.suppression_duration = AAZStrType(
                serialized_name="suppressionDuration",
                flags={"required": True},
            )
            properties.suppression_enabled = AAZBoolType(
                serialized_name="suppressionEnabled",
                flags={"required": True},
            )
            properties.tactics = AAZListType()
            properties.techniques = AAZListType()
            properties.template_version = AAZStrType(
                serialized_name="templateVersion",
            )

            custom_details = cls._schema_on_200.discriminate_by("kind", "NRT").properties.custom_details
            custom_details.Element = AAZStrType()

            tactics = cls._schema_on_200.discriminate_by("kind", "NRT").properties.tactics
            tactics.Element = AAZStrType()

            techniques = cls._schema_on_200.discriminate_by("kind", "NRT").properties.techniques
            techniques.Element = AAZStrType()

            disc_scheduled = cls._schema_on_200.discriminate_by("kind", "Scheduled")
            disc_scheduled.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.discriminate_by("kind", "Scheduled").properties
            properties.alert_details_override = AAZObjectType(
                serialized_name="alertDetailsOverride",
            )
            _build_schema_alert_details_override_read(properties.alert_details_override)
            properties.alert_rule_template_name = AAZStrType(
                serialized_name="alertRuleTemplateName",
            )
            properties.custom_details = AAZDictType(
                serialized_name="customDetails",
            )
            properties.description = AAZStrType()
            properties.display_name = AAZStrType(
                serialized_name="displayName",
                flags={"required": True},
            )
            properties.enabled = AAZBoolType(
                flags={"required": True},
            )
            properties.entity_mappings = AAZListType(
                serialized_name="entityMappings",
            )
            _build_schema_entity_mappings_read(properties.entity_mappings)
            properties.event_grouping_settings = AAZObjectType(
                serialized_name="eventGroupingSettings",
            )
            properties.incident_configuration = AAZObjectType(
                serialized_name="incidentConfiguration",
            )
            _build_schema_incident_configuration_read(properties.incident_configuration)
            properties.last_modified_utc = AAZStrType(
                serialized_name="lastModifiedUtc",
                flags={"read_only": True},
            )
            properties.query = AAZStrType(
                flags={"required": True},
            )
            properties.query_frequency = AAZStrType(
                serialized_name="queryFrequency",
                flags={"required": True},
            )
            properties.query_period = AAZStrType(
                serialized_name="queryPeriod",
                flags={"required": True},
            )
            properties.severity = AAZStrType(
                flags={"required": True},
            )
            properties.suppression_duration = AAZStrType(
                serialized_name="suppressionDuration",
                flags={"required": True},
            )
            properties.suppression_enabled = AAZBoolType(
                serialized_name="suppressionEnabled",
                flags={"required": True},
            )
            properties.tactics = AAZListType()
            properties.techniques = AAZListType()
            properties.template_version = AAZStrType(
                serialized_name="templateVersion",
            )
            properties.trigger_operator = AAZStrType(
                serialized_name="triggerOperator",
                flags={"required": True},
            )
            properties.trigger_threshold = AAZIntType(
                serialized_name="triggerThreshold",
                flags={"required": True},
            )

            custom_details = cls._schema_on_200.discriminate_by("kind", "Scheduled").properties.custom_details
            custom_details.Element = AAZStrType()

            event_grouping_settings = cls._schema_on_200.discriminate_by("kind", "Scheduled").properties.event_grouping_settings
            event_grouping_settings.aggregation_kind = AAZStrType(
                serialized_name="aggregationKind",
            )

            tactics = cls._schema_on_200.discriminate_by("kind", "Scheduled").properties.tactics
            tactics.Element = AAZStrType()

            techniques = cls._schema_on_200.discriminate_by("kind", "Scheduled").properties.techniques
            techniques.Element = AAZStrType()

            disc_threat_intelligence = cls._schema_on_200.discriminate_by("kind", "ThreatIntelligence")
            disc_threat_intelligence.properties = AAZObjectType(
                flags={"client_flatten": True},
            )

            properties = cls._schema_on_200.discriminate_by("kind", "ThreatIntelligence").properties
            properties.alert_rule_template_name = AAZStrType(
                serialized_name="alertRuleTemplateName",
                flags={"required": True},
            )
            properties.description = AAZStrType(
                flags={"read_only": True},
            )
            properties.display_name = AAZStrType(
                serialized_name="displayName",
                flags={"read_only": True},
            )
            properties.enabled = AAZBoolType(
                flags={"required": True},
            )
            properties.last_modified_utc = AAZStrType(
                serialized_name="lastModifiedUtc",
                flags={"read_only": True},
            )
            properties.severity = AAZStrType(
                flags={"read_only": True},
            )
            properties.tactics = AAZListType(
                flags={"read_only": True},
            )
            properties.techniques = AAZListType(
                flags={"read_only": True},
            )

            tactics = cls._schema_on_200.discriminate_by("kind", "ThreatIntelligence").properties.tactics
            tactics.Element = AAZStrType(
                flags={"read_only": True},
            )

            techniques = cls._schema_on_200.discriminate_by("kind", "ThreatIntelligence").properties.techniques
            techniques.Element = AAZStrType(
                flags={"read_only": True},
            )

            return cls._schema_on_200


_schema_alert_details_override_read = None


def _build_schema_alert_details_override_read(_schema):
    global _schema_alert_details_override_read
    if _schema_alert_details_override_read is not None:
        _schema.alert_description_format = _schema_alert_details_override_read.alert_description_format
        _schema.alert_display_name_format = _schema_alert_details_override_read.alert_display_name_format
        _schema.alert_severity_column_name = _schema_alert_details_override_read.alert_severity_column_name
        _schema.alert_tactics_column_name = _schema_alert_details_override_read.alert_tactics_column_name
        return

    _schema_alert_details_override_read = AAZObjectType()

    alert_details_override_read = _schema_alert_details_override_read
    alert_details_override_read.alert_description_format = AAZStrType(
        serialized_name="alertDescriptionFormat",
    )
    alert_details_override_read.alert_display_name_format = AAZStrType(
        serialized_name="alertDisplayNameFormat",
    )
    alert_details_override_read.alert_severity_column_name = AAZStrType(
        serialized_name="alertSeverityColumnName",
    )
    alert_details_override_read.alert_tactics_column_name = AAZStrType(
        serialized_name="alertTacticsColumnName",
    )

    _schema.alert_description_format = _schema_alert_details_override_read.alert_description_format
    _schema.alert_display_name_format = _schema_alert_details_override_read.alert_display_name_format
    _schema.alert_severity_column_name = _schema_alert_details_override_read.alert_severity_column_name
    _schema.alert_tactics_column_name = _schema_alert_details_override_read.alert_tactics_column_name


_schema_entity_mappings_read = None


def _build_schema_entity_mappings_read(_schema):
    global _schema_entity_mappings_read
    if _schema_entity_mappings_read is not None:
        _schema.Element = _schema_entity_mappings_read.Element
        return

    _schema_entity_mappings_read = AAZListType()

    entity_mappings_read = _schema_entity_mappings_read
    entity_mappings_read.Element = AAZObjectType()

    _element = _schema_entity_mappings_read.Element
    _element.entity_type = AAZStrType(
        serialized_name="entityType",
    )
    _element.field_mappings = AAZListType(
        serialized_name="fieldMappings",
    )

    field_mappings = _schema_entity_mappings_read.Element.field_mappings
    field_mappings.Element = AAZObjectType()

    _element = _schema_entity_mappings_read.Element.field_mappings.Element
    _element.column_name = AAZStrType(
        serialized_name="columnName",
    )
    _element.identifier = AAZStrType()

    _schema.Element = _schema_entity_mappings_read.Element


_schema_incident_configuration_read = None


def _build_schema_incident_configuration_read(_schema):
    global _schema_incident_configuration_read
    if _schema_incident_configuration_read is not None:
        _schema.create_incident = _schema_incident_configuration_read.create_incident
        _schema.grouping_configuration = _schema_incident_configuration_read.grouping_configuration
        return

    _schema_incident_configuration_read = AAZObjectType()

    incident_configuration_read = _schema_incident_configuration_read
    incident_configuration_read.create_incident = AAZBoolType(
        serialized_name="createIncident",
        flags={"required": True},
    )
    incident_configuration_read.grouping_configuration = AAZObjectType(
        serialized_name="groupingConfiguration",
    )

    grouping_configuration = _schema_incident_configuration_read.grouping_configuration
    grouping_configuration.enabled = AAZBoolType(
        flags={"required": True},
    )
    grouping_configuration.group_by_alert_details = AAZListType(
        serialized_name="groupByAlertDetails",
    )
    grouping_configuration.group_by_custom_details = AAZListType(
        serialized_name="groupByCustomDetails",
    )
    grouping_configuration.group_by_entities = AAZListType(
        serialized_name="groupByEntities",
    )
    grouping_configuration.lookback_duration = AAZStrType(
        serialized_name="lookbackDuration",
        flags={"required": True},
    )
    grouping_configuration.matching_method = AAZStrType(
        serialized_name="matchingMethod",
        flags={"required": True},
    )
    grouping_configuration.reopen_closed_incident = AAZBoolType(
        serialized_name="reopenClosedIncident",
        flags={"required": True},
    )

    group_by_alert_details = _schema_incident_configuration_read.grouping_configuration.group_by_alert_details
    group_by_alert_details.Element = AAZStrType()

    group_by_custom_details = _schema_incident_configuration_read.grouping_configuration.group_by_custom_details
    group_by_custom_details.Element = AAZStrType()

    group_by_entities = _schema_incident_configuration_read.grouping_configuration.group_by_entities
    group_by_entities.Element = AAZStrType()

    _schema.create_incident = _schema_incident_configuration_read.create_incident
    _schema.grouping_configuration = _schema_incident_configuration_read.grouping_configuration


__all__ = ["Show"]