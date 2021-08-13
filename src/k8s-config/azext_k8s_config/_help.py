# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import

helps['k8s-config'] = """
    type: group
    short-summary: Commands to manage resources from Microsoft.KubernetesConfiguration.
"""

helps['k8s-config flux'] = """
    type: group
    short-summary: Commands to manage Flux V2 Kubernetes configurations.
"""

helps['k8s-config flux create'] = """
    type: command
    short-summary: Create a Kubernetes Flux Configuration.
    examples:
      - name: Create a Kubernetes Flux Configuration
        text: |-
          az k8s-config flux create --resource-group my-resource-group --cluster-name mycluster \\
          --cluster-type connectedClusters --name myconfig --scope cluster --namespace my-namespace \\
          --kind git --url https://github.com/Azure/arc-k8s-demo --branch main --kustomization \\
          name=my-kustomization path="./apps"
      - name: Create a Kubernetes Flux Configuration with Multiple Kustomizations
        text: |-
          az k8s-config flux create --resource-group my-resource-group --cluster-name mycluster \\
          --cluster-type connectedClusters --name myconfig --scope cluster --namespace my-namespace \\
          --kind git --url https://github.com/Azure/arc-k8s-demo --https-user my-username \\
          --https-key my-password --branch main --kustomization name=my-crds path="./crds" \\
          --kustomization name=my-apps path="./apps" depends_on=my-crds timeout=PT5M
"""

helps['k8s-config flux list'] = """
    type: command
    short-summary: List Kubernetes Flux Configurations.
    examples:
      - name: List all Kubernetes Flux Configurations on a cluster
        text: |-
          az k8s-config flux list --resource-group my-resource-group --cluster-name mycluster \\
          --cluster-type connectedClusters
"""

helps['k8s-config flux show'] = """
    type: command
    short-summary: Show a Kubernetes Flux Configuration.
    examples:
      - name: Show details of a Kubernetes Flux Configuration
        text: |-
          az k8s-config flux show --resource-group my-resource-group --cluster-name mycluster \\
          --cluster-type connectedClusters --name myconfig
"""

helps['k8s-config flux delete'] = """
    type: command
    short-summary: Delete a Kubernetes Flux Configuration.
    examples:
      - name: Delete an existing Kubernetes Flux Configuration
        text: |-
          az k8s-config flux delete --resource-group my-resource-group --cluster-name mycluster \\
          --cluster-type connectedClusters --name myconfig
"""

helps['k8s-config extension'] = """
    type: group
    short-summary: Commands to manage Flux V2 Kubernetes configurations.
"""

helps['k8s-config extension create'] = """
    type: command
    short-summary: Create a Kubernetes Extension.
    examples:
      - name: Create a Kubernetes Extension
        text: |-
          az k8s-config extension create --resource-group my-resource-group --cluster-name mycluster \\
          --cluster-type connectedClusters --name myextension --extension-type microsoft.openservicemesh \\
          --scope cluster --release-train stable
"""

helps['k8s-config extension list'] = """
    type: command
    short-summary: List Kubernetes Flux Configurations.
    examples:
      - name: List all Kubernetes Flux Configurations on a cluster
        text: |-
          az k8s-config extension list --resource-group my-resource-group --cluster-name mycluster \\
          --cluster-type connectedClusters
"""

helps['k8s-config extension show'] = """
    type: command
    short-summary: Show a Kubernetes Flux Configuration.
    examples:
      - name: Show details of a Kubernetes Flux Configuration
        text: |-
          az k8s-config extension show --resource-group my-resource-group --cluster-name mycluster \\
          --cluster-type connectedClusters --name myextension
"""

helps['k8s-config extension delete'] = """
    type: command
    short-summary: Delete a Kubernetes Flux Configuration.
    examples:
      - name: Delete an existing Kubernetes Flux Configuration
        text: |-
          az k8s-config extension delete --resource-group my-resource-group --cluster-name mycluster \\
          --cluster-type connectedClusters --name myextension
"""
