# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""This module contains a class representing method calls that are received and responded to.
"""


class MethodCall(object):
    """Represents a call to a device or module method.

    :ivar str name: The name of the method being called.
    :ivar payload: The payload being sent with the call.
    """

    def __init__(self, request_id, name, payload):
        """Initializer for a MethodCall.

        :param str request_id: The request id of the method being called.
        :param str name: The name of the method being called.
        :param payload: The payload being sent with the call.
        """
        self._request_id = request_id
        self._name = name
        self._payload = payload

    @property
    def name(self):
        return self._name

    @property
    def payload(self):
        return self._payload
