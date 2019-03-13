# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""
This module contains one of the implementations of the Registration Client which uses Symmetric Key authentication.
"""
import logging
from .registration_client import RegistrationClient

logger = logging.getLogger(__name__)


class SymmetricKeyRegistrationClient(RegistrationClient):
    """
    Client which can be used to run the registration of a device using Symmetric Key authentication.
    """

    def __init__(self, transport):
        """
        Initializer for the Symmetric Key Registration Client
        """
        RegistrationClient.__init__(self, transport)
        self.transport.on_registration_complete = self.on_device_registration_complete

    def register(self):
        self.transport.send_registration_request()

    def cancel(self):
        pass

    def on_device_registration_complete(self, topic, payload):
        logger.info("on_device_registration_complete")
        self.on_registration_complete(topic, payload)
