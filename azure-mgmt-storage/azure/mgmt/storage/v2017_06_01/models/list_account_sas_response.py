# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ListAccountSasResponse(Model):
    """The List SAS credentials operation response.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar account_sas_token: List SAS credentials of storage account.
    :vartype account_sas_token: str
    """

    _validation = {
        'account_sas_token': {'readonly': True},
    }

    _attribute_map = {
        'account_sas_token': {'key': 'accountSasToken', 'type': 'str'},
    }

    def __init__(self):
        super(ListAccountSasResponse, self).__init__()
        self.account_sas_token = None
