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


class SuggestedActions(Model):
    """SuggestedActions that can be performed.

    :param to: Ids of the recipients that the actions should be shown to.
     These Ids are relative to the channelId and a subset of all recipients of
     the activity
    :type to: list[str]
    :param actions: Actions that can be shown to the user
    :type actions: list[~bot.connector.models.CardAction]
    """

    _attribute_map = {
        'to': {'key': 'to', 'type': '[str]'},
        'actions': {'key': 'actions', 'type': '[CardAction]'},
    }

    def __init__(self, to=None, actions=None):
        super(SuggestedActions, self).__init__()
        self.to = to
        self.actions = actions
