# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""
This module provides an abstract interface representing clients which can communicate with the
Device Provisioning Service.
"""

import abc
import six


@six.add_metaclass(abc.ABCMeta)
class RegistrationClient(object):
    """
    Super class for any client that can be used to register devices to Device Provisioning Service.
    :ivar str provisioning_host: Host running the Device Provisioning Service.
    :ivar str security_client: Instance of Security client
    :ivar str module_id: Instance of transport.
    """

    def __init__(self, transport):
        """
        Initializes the registration client.
        :param transport: Instance of the Transport object.
        """
        self.transport = transport

    @abc.abstractmethod
    def register(self):
        """
        Register the device with the Device Provisioning Service.
        """
        pass

    @abc.abstractmethod
    def cancel(self):
        """
        Cancel an in progress registration of the device with the Device Provisioning Service.
        """
        pass
