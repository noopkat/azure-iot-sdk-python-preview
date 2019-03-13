# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import abc
import six


@six.add_metaclass(abc.ABCMeta)
class SymmetricKeyTransport(object):
    """
    A super class of transports that use shared access signature token to connect.
    """

    def __init__(self, symmetric_key_security_provider):
        self.security_provider = symmetric_key_security_provider

    def get_current_sas_token(self):
        """
        Set the current Shared Access Signature Token string.
        """
        return self.security_provider.create_shared_access_signature()
