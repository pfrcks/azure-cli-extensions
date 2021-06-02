# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long

# ERROR/HELP TEXT DEFINITIONS -----------------------------------------

KUSTOMIZATION_REQUIRED_VALUES_MISSING_ERROR = "Error! Kustomization definition is invalid, required values {} not found"
KUSTOMIZATION_REQUIRED_VALUES_MISSING_HELP = "Add the required values to the Kustomization object and try again"

REPOSITORY_REF_REQUIRED_VALUES_MISSING_ERROR = "Error! Repository reference is invalid"
REPOSITORY_REF_REQUIRED_VALUES_MISSING_HELP = "Specifying one of [--branch, --tag, --semver, --commit] is required"

GIT_REPOSITORY_REQUIRED_VALUES_MISSING_ERROR = "Error! Git repository kind is missing required value {}"
GIT_REPOSITORY_REQUIRED_VALUES_MISSING_HELP = "Add missing git repository kind and try again"

INVALID_DURATION_ERROR = "Error! Invalid {0}."
INVALID_DURATION_HELP = "Specify a valid ISO8601 duration and try again"

INVALID_URL_ERROR = "Error! Invalid --url."
INVALID_URL_HELP = "Url must beginwith one of ['http://', 'https://', 'git@', 'ssh://']"

INVALID_KUBERNETES_NAME_LENGTH_ERROR = "Error! Invalid {0}."
INVALID_KUBERNETES_NAME_LENGTH_HELP = "Parameter {0} can be a maximum of {1} characters. Specify a shorter name and try again."

INVALID_KUBERNETES_NAME_HYPHEN_ERROR = "Error! Invalid {0}."
INVALID_KUBERNETES_NAME_HYPHEN_HELP = "Parameter {0} cannot begin or end with a hyphen."

INVALID_KUBERNETES_NAME_ERROR = "Error! Invalid {0}."
INVALID_KUBERNETES_NAME_HELP = "Parameter {0} can only contain lowercase alphanumeric characters and hyphens"

DUPLICATE_KUSTOMIZATION_NAME_ERROR = "Error! Invalid Kustomization list. Kustomization name {0} duplicated in multiple Kustomization objects"
DUPLICATE_KUSTOMIZATION_NAME_HELP = "Ensure that all Kustomization names are unique and try again"

SSH_PRIVATE_KEY_WITH_HTTP_URL_ERROR = "Error! An --ssh-private-key cannot be used with an http(s) url"
SSH_PRIVATE_KEY_WITH_HTTP_URL_HELP = "Verify the url provided is a valid ssh url and not an http(s) url"

KNOWN_HOSTS_WITH_HTTP_URL_ERROR = "Error! --ssh-known-hosts cannot be used with an http(s) url"
KNOWN_HOSTS_WITH_HTTP_URL_HELP = "Verify the url provided is a valid ssh url and not an http(s) url"

HTTPS_AUTH_WITH_SSH_URL_ERROR = "Error! https auth (--https-user and --https-key) cannot be used with a non-http(s) url"
HTTPS_AUTH_WITH_SSH_URL_HELP = "Verify the url provided is a valid http(s) url and not an ssh url"

KNOWN_HOSTS_BASE64_ENCODING_ERROR = "Error! ssh known_hosts is not a valid utf-8 base64 encoded string"
KNOWN_HOSTS_BASE64_ENCODING_HELP = "Verify that the string provided safely decodes into a valid utf-8 format"

KNOWN_HOSTS_FORMAT_ERROR = "Error! ssh known_hosts provided in wrong format"
KNOWN_HOSTS_FORMAT_HELP = "Verify that all lines in the known_hosts contents are provided in a valid sshd(8) format"

SSH_PRIVATE_KEY_ERROR = "Error! --ssh-private-key provided in invalid format"
SSH_PRIVATE_KEY_HELP = "Verify the key provided is a valid PEM-formatted key of type RSA, ECC, DSA, or Ed25519"

HTTPS_USER_WITHOUT_KEY_ERROR = "Error! --https-user used without --https-key"
HTTPS_USER_WITHOUT_KEY_HELP = "Try providing both --https-user and --https-key together"

HTTPS_KEY_WITHOUT_USER_ERROR = "Error! --http-key used without --http-user"
HTTPS_KEY_WITHOUT_USER_HELP = "Try providing both --https-user and --https-key together"

KEY_FILE_READ_ERROR = "Error! Unable to read key file specified with: {0}"
KEY_FILE_READ_HELP = "Verify that the filepath specified exists and contains valid utf-8 data"

KEY_AND_FILE_TOGETHER_ERROR = "Error! Both textual key and key filepath cannot be provided"
KEY_AND_FILE_TOGETHER_HELP = "Try providing the file parameter without providing the plaintext parameter"

HTTP_URL_NO_AUTH_WARNING = "Warning! https url is being used without https auth params, ensure the repository url provided is not a private repo"

# PROVIDER REGISTRATION -----------------------------------------

CC_REGISTRATION_WARNING = "'Flux Configuration' cannot be used because '{0}' provider has not been registered. More details for registering this provider can be found here - {1}"
CC_REGISTRATION_LINK = "https://aka.ms/RegisterKubernetesConfigurationProvider"
CC_REGISTRATION_ERROR = "Unable to fetch registration state of '{0}' provider. Failed to enable 'flux configuration' feature..."
CC_PROVIDER_NAMESPACE = 'Microsoft.KubernetesConfiguration'
REGISTERED = "Registered"

SSH_PRIVATE_KEY_KEY = "sshPrivateKey"
HTTPS_USER_KEY = "httpsUser"
HTTPS_KEY_KEY = "httpsKey"

DEPENDENCY_KEYS = ["dependencies", "depends_on"]
SYNC_INTERVAL_KEYS = ["interval", "sync_interval"]
TIMEOUT_KEY = "timeout"
REQUIRED_KUSTOMIZATION_KEYS = {"name", "path"}

VALID_ISO8601_DURATION_REGEX = r"^P(?!$)(\d+Y)?(\d+M)?(\d+W)?(\d+D)?(T(?=\d)(\d+H)?(\d+M)?(\d+S)?)?$"
VALID_URL_REGEX = r"^(((http|https|ssh)://)|(git@))"
VALID_KUBERNETES_NAME_REGEX = r"^[a-z0-9]([-a-z0-9]*[a-z0-9])?$"

GIT = "git"
GIT_REPOSITORY = "GitRepository"

CONNECTED_CLUSTERS = "connectedclusters"
MANAGED_CLUSTERS = "managedclusters"

MANAGED_RP_NAMESPACE = "Microsoft.ContainerService"
CONNECTED_RP_NAMESPACE = "Microsoft.Kubernetes"
