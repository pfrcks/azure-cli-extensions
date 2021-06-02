# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=protected-access

import argparse
from azure.cli.core.azclierror import InvalidArgumentValueError
from .vendored_sdks.models import KustomizationDefinition
from .validators import validate_kustomization
from . import consts
from .utils import parse_dependencies


class KustomizationAddAction(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        validate_kustomization(values)
        dependencies = []
        sync_interval = ""
        kwargs = {}
        for item in values:
            try:
                key, value = item.split('=', 1)
                if key in consts.DEPENDENCY_KEYS:
                    dependencies = parse_dependencies(value)
                elif key in consts.SYNC_INTERVAL_KEYS:
                    sync_interval = value
                else:
                    kwargs[key] = value
            except ValueError:
                raise InvalidArgumentValueError('usage error: {} KEY=VALUE [KEY=VALUE ...]'.format(option_string))
        super(KustomizationAddAction, self).__call__(
            parser,
            namespace,
            KustomizationDefinition(depends_on=dependencies, sync_interval=sync_interval, **kwargs),
            option_string
        )
