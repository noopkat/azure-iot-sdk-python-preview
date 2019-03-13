# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""
This module provides factory methods for creating clients which would
communicate with Device Provisioning Service.
"""
from ..security.sk_security_provider import SymmetricKeySecurityProvider
from ..transport.mqtt_transport import MQTTTransport
from .sk_registration_client import SymmetricKeyRegistrationClient


def create_from_security_provider(provisioning_host, security_provider, transport_choice):
    """
    Creates different types of registration clients which can enable devices to communicate with Device Provisioning
    Service based on parameters passed.
    :param provisioning_host: Host running the Device Provisioning Service. Can be found in the Azure portal in the
    Overview tab as the string Global device endpoint
    :param security_provider: Instance of Security client object which can be either of Symmetric Key, TPM or X.509
    :param transport_choice: A string representing the transport the user wants
    :return: A specific registration client based on parameters and validations.
    """
    if not provisioning_host:
        raise ValueError("Provisioning Host must be provided.")

    if transport_choice == "mqtt":
        if isinstance(security_provider, SymmetricKeySecurityProvider):
            mqtt_transport = MQTTTransport(provisioning_host, security_provider)
            return SymmetricKeyRegistrationClient(mqtt_transport)
            # TODO : other instances of security provider can also be checked before creating mqtt
        else:
            raise ValueError(
                " A symmetric key security provider must be provided for instantiating MQTT"
            )
        # TODO : Message must be enhanced later for other security providers. MQTT can also support X509.
