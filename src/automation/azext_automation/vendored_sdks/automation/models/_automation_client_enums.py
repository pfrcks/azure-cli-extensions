# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class AutomationAccountState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Gets status of account.
    """

    OK = "Ok"
    UNAVAILABLE = "Unavailable"
    SUSPENDED = "Suspended"

class AutomationKeyName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Automation key name.
    """

    PRIMARY = "Primary"
    SECONDARY = "Secondary"

class AutomationKeyPermissions(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Automation key permissions.
    """

    READ = "Read"
    FULL = "Full"

class HttpStatusCode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    CONTINUE_ENUM = "Continue"
    SWITCHING_PROTOCOLS = "SwitchingProtocols"
    OK = "OK"
    CREATED = "Created"
    ACCEPTED = "Accepted"
    NON_AUTHORITATIVE_INFORMATION = "NonAuthoritativeInformation"
    NO_CONTENT = "NoContent"
    RESET_CONTENT = "ResetContent"
    PARTIAL_CONTENT = "PartialContent"
    MULTIPLE_CHOICES = "MultipleChoices"
    AMBIGUOUS = "Ambiguous"
    MOVED_PERMANENTLY = "MovedPermanently"
    MOVED = "Moved"
    FOUND = "Found"
    REDIRECT = "Redirect"
    SEE_OTHER = "SeeOther"
    REDIRECT_METHOD = "RedirectMethod"
    NOT_MODIFIED = "NotModified"
    USE_PROXY = "UseProxy"
    UNUSED = "Unused"
    TEMPORARY_REDIRECT = "TemporaryRedirect"
    REDIRECT_KEEP_VERB = "RedirectKeepVerb"
    BAD_REQUEST = "BadRequest"
    UNAUTHORIZED = "Unauthorized"
    PAYMENT_REQUIRED = "PaymentRequired"
    FORBIDDEN = "Forbidden"
    NOT_FOUND = "NotFound"
    METHOD_NOT_ALLOWED = "MethodNotAllowed"
    NOT_ACCEPTABLE = "NotAcceptable"
    PROXY_AUTHENTICATION_REQUIRED = "ProxyAuthenticationRequired"
    REQUEST_TIMEOUT = "RequestTimeout"
    CONFLICT = "Conflict"
    GONE = "Gone"
    LENGTH_REQUIRED = "LengthRequired"
    PRECONDITION_FAILED = "PreconditionFailed"
    REQUEST_ENTITY_TOO_LARGE = "RequestEntityTooLarge"
    REQUEST_URI_TOO_LONG = "RequestUriTooLong"
    UNSUPPORTED_MEDIA_TYPE = "UnsupportedMediaType"
    REQUESTED_RANGE_NOT_SATISFIABLE = "RequestedRangeNotSatisfiable"
    EXPECTATION_FAILED = "ExpectationFailed"
    UPGRADE_REQUIRED = "UpgradeRequired"
    INTERNAL_SERVER_ERROR = "InternalServerError"
    NOT_IMPLEMENTED = "NotImplemented"
    BAD_GATEWAY = "BadGateway"
    SERVICE_UNAVAILABLE = "ServiceUnavailable"
    GATEWAY_TIMEOUT = "GatewayTimeout"
    HTTP_VERSION_NOT_SUPPORTED = "HttpVersionNotSupported"

class JobProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The provisioning state of the resource.
    """

    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    SUSPENDED = "Suspended"
    PROCESSING = "Processing"

class JobStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Gets or sets the status of the job.
    """

    NEW = "New"
    ACTIVATING = "Activating"
    RUNNING = "Running"
    COMPLETED = "Completed"
    FAILED = "Failed"
    STOPPED = "Stopped"
    BLOCKED = "Blocked"
    SUSPENDED = "Suspended"
    DISCONNECTED = "Disconnected"
    SUSPENDING = "Suspending"
    STOPPING = "Stopping"
    RESUMING = "Resuming"
    REMOVING = "Removing"

class JobStreamType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Gets or sets the stream type.
    """

    PROGRESS = "Progress"
    OUTPUT = "Output"
    WARNING = "Warning"
    ERROR = "Error"
    DEBUG = "Debug"
    VERBOSE = "Verbose"
    ANY = "Any"

class RunbookState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Gets or sets the state of the runbook.
    """

    NEW = "New"
    EDIT = "Edit"
    PUBLISHED = "Published"

class RunbookTypeEnum(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Gets or sets the type of the runbook.
    """

    SCRIPT = "Script"
    GRAPH = "Graph"
    POWER_SHELL_WORKFLOW = "PowerShellWorkflow"
    POWER_SHELL = "PowerShell"
    GRAPH_POWER_SHELL_WORKFLOW = "GraphPowerShellWorkflow"
    GRAPH_POWER_SHELL = "GraphPowerShell"

class SkuNameEnum(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Gets or sets the SKU name of the account.
    """

    FREE = "Free"
    BASIC = "Basic"
