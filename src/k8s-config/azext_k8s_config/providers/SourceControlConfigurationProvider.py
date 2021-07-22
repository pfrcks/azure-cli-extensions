from azext_k8s_config.validators import validate_cc_registration, validate_known_hosts, validate_url_with_params
from azure.cli.core.azclierror import ResourceNotFoundError
from azure.core.exceptions import HttpResponseError
from knack.log import get_logger

from .._client_factory import k8s_config_sourcecontrol_client
from ..utils import fix_compliance_state, get_cluster_rp, get_data_from_key_or_file, get_protected_settings

from ..vendored_sdks.v2021_03_01.models import (
    HelmOperatorProperties,
    SourceControlConfiguration
)

logger = get_logger(__name__)


class SourceControlConfigurationProvider:
    def __init__(self, cmd):
        self.cmd = cmd
        self.client = k8s_config_sourcecontrol_client(cmd.cli_ctx)

    
    def show(self, resource_group_name, cluster_type, cluster_name, name):
        # Determine ClusterRP
        cluster_rp = get_cluster_rp(cluster_type)
        try:
            extension = self.client.get(resource_group_name,
                                cluster_rp, cluster_type, cluster_name, name)
            return extension
        except HttpResponseError as ex:
            # Customize the error message for resources not found
            if ex.response.status_code == 404:
                # If Cluster not found
                if ex.message.__contains__("(ResourceNotFound)"):
                    message = "{0} Verify that the cluster-type is correct and the resource exists.".format(
                        ex.message)
                # If Configuration not found
                elif ex.message.__contains__("Operation returned an invalid status code 'Not Found'"):
                    message = "(SourceControlConfigurationNotFound) The Resource {0}/{1}/{2}/Microsoft.KubernetesConfiguration/" \
                            "sourceControlConfigurations/{3} could not be found!".format(
                                self.cluster_rp, self.cluster_type, self.cluster_name, self.name)
                else:
                    message = ex.message
                raise ResourceNotFoundError(message)


    def list(self, resource_group_name, cluster_type, cluster_name):
        cluster_rp = get_cluster_rp(cluster_type)
        return self.client.list(resource_group_name, cluster_rp, cluster_type, cluster_name)

    
    def delete(self, resource_group_name, cluster_type, cluster_name, name):
        cluster_rp = get_cluster_rp(cluster_type)
        return self.client.begin_delete(resource_group_name, cluster_rp, cluster_type, cluster_name, name)

    # pylint: disable=too-many-locals
    def create(self, resource_group_name, cluster_name, name, repository_url, scope, cluster_type,
               operator_instance_name, operator_namespace, helm_operator_chart_version, operator_type,
               operator_params, ssh_private_key, ssh_private_key_file, https_user, https_key,
               ssh_known_hosts, ssh_known_hosts_file, enable_helm_operator, helm_operator_params):
        
        """Create a new Kubernetes Source Control Configuration.

        """
        # Determine ClusterRP
        cluster_rp = get_cluster_rp(cluster_type)

        # Determine operatorInstanceName
        if operator_instance_name is None:
            operator_instance_name = name

        # Create helmOperatorProperties object
        helm_operator_properties = None
        if enable_helm_operator:
            helm_operator_properties = HelmOperatorProperties()
            helm_operator_properties.chart_version = helm_operator_chart_version.strip()
            helm_operator_properties.chart_values = helm_operator_params.strip()

        protected_settings = get_protected_settings(ssh_private_key,
                                                    ssh_private_key_file,
                                                    https_user,
                                                    https_key)
        knownhost_data = get_data_from_key_or_file(ssh_known_hosts, ssh_known_hosts_file)
        if knownhost_data:
            validate_known_hosts(knownhost_data)

        # Flag which parameters have been set and validate these settings against the set repository url
        ssh_private_key_set = ssh_private_key != '' or ssh_private_key_file != ''
        known_hosts_contents_set = knownhost_data != ''
        https_auth_set = https_user != '' and https_key != ''
        validate_url_with_params(repository_url,
                                 ssh_private_key_set=ssh_private_key_set,
                                 known_hosts_contents_set=known_hosts_contents_set,
                                 https_auth_set=https_auth_set)

        # Validate that the subscription is registered to Microsoft.KubernetesConfiguration
        validate_cc_registration(self.cmd)

        # Create sourceControlConfiguration object
        source_control_configuration = SourceControlConfiguration(
            repository_url=repository_url,
            operator_namespace=operator_namespace,
            operator_instance_name=operator_instance_name,
            operator_type=operator_type,
            operator_params=operator_params,
            configuration_protected_settings=protected_settings,
            operator_scope=scope,
            ssh_known_hosts_contents=knownhost_data,
            enable_helm_operator=enable_helm_operator,
            helm_operator_properties=helm_operator_properties
        )

        # Try to create the resource
        config = self.client.create_or_update(resource_group_name, cluster_rp, cluster_type, cluster_name,
                                              name, source_control_configuration)

        return fix_compliance_state(config)