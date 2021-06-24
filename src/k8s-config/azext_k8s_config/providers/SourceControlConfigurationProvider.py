from azure.cli.core.azclierror import ResourceNotFoundError
from azure.core.exceptions import HttpResponseError
from knack.log import get_logger

from .._client_factory import k8s_config_sourcecontrol_client
from ..utils import get_cluster_rp

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
        return self.client.delete(resource_group_name, cluster_rp, cluster_type, cluster_name, name)


    def create():
        pass