# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import uuid
import logging
import six.moves.urllib as urllib
from . import device_provisioning_constant
from azure.iot.hub.devicesdk.transport.mqtt.mqtt_provider import MQTTProvider
from .symmetric_key_transport import SymmetricKeyTransport

logger = logging.getLogger(__name__)


class MQTTTransport(SymmetricKeyTransport):
    def __init__(self, provisioning_host, security_provider):
        SymmetricKeyTransport.__init__(self, security_provider)
        self._provisioning_host = provisioning_host
        self._create_mqtt_provider()

    def send_registration_request(self):
        self._connect()

        rid = uuid.uuid4()
        topic = "$dps/registrations/PUT/iotdps-register/?$rid=" + str(rid)
        self._mqtt_provider.publish(topic, " ")

    def query_operation_status(self):
        pass

    def disconnect(self):
        logger.info("Calling provider disconnect")
        self._mqtt_provider.disconnect()

    def _connect(self):
        logger.info("Calling provider connect")
        password = self.get_current_sas_token()
        self._mqtt_provider.connect(password)

    def _create_mqtt_provider(self):
        client_id = self.security_provider.registration_id

        username = (
            self.security_provider.id_scope
            + "/registrations/"
            + self.security_provider.registration_id
            + "/api-version="
            + device_provisioning_constant.API_VERSION
            + "&ClientVersion="
            + urllib.parse.quote_plus(device_provisioning_constant.USER_AGENT)
        )

        hostname = self._provisioning_host

        self._mqtt_provider = MQTTProvider(client_id, hostname, username, ca_cert=None)

        self._mqtt_provider.on_mqtt_connected = self._on_provider_connect_complete
        self._mqtt_provider.on_mqtt_disconnected = self._on_provider_disconnect_complete
        self._mqtt_provider.on_mqtt_published = self._on_provider_publish_complete
        self._mqtt_provider.on_mqtt_subscribed = self._on_provider_subscribe_complete
        self._mqtt_provider.on_mqtt_message_received = self.on_provider_message_received_callback

    def _on_provider_connect_complete(self):
        logger.info("_on_provider_connect_complete")
        topic = "$dps/registrations/res/#"
        self._mqtt_provider.subscribe(topic, 1)

    def _on_provider_disconnect_complete(self):
        logger.info("_on_provider_disconnect_complete")

    def _on_provider_publish_complete(self, mid):
        logger.info("_on_provider_publish_complete")

    def _on_provider_subscribe_complete(self, mid):
        logger.info("_on_provider_subscribe_complete")

    def on_provider_message_received_callback(self, topic, payload):
        logger.info("Message received on topic %s", topic)
        logger.info("Message has been received")
        self.on_registration_complete(topic, payload)
