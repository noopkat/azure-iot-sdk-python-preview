# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""
This module contains constants related to the transport package.
"""

USER_AGENT = "azure-iot-provisioning-device" + "/" + "1.5.3"
"""
Default interval for polling, to use in case service doesn't provide it to us.
"""
POLLING_INTERVAL = 2000

"""
api version to use while communicating with service.
"""
API_VERSION = "2018-11-01"
"""
Timeout to use when communicating with the service
"""
DEFAULT_TIMEOUT = 30000
