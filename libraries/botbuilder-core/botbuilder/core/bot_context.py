# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import sys
from copy import deepcopy
from uuid import uuid4
from typing import List
from botbuilder.schema import Activity, ActivityTypes, ConversationReference

# from .bot_adapter import BotAdapter
from .assertions import BotAssert


class BotContext(object):
    def __init__(self, adapter, activity: Activity=None, reference: ConversationReference=None):
        self._adapter = adapter
        self.reference: ConversationReference = reference
        self.request: Activity = activity
        self.responses: List[Activity] = []
        self._services: dict = {}

        if self.request is not None:
            self.reference = ConversationReference(activity_id=activity.id,
                                                   user=activity.from_property,
                                                   bot=activity.recipient,
                                                   conversation=activity.conversation,
                                                   channel_id=activity.channel_id,
                                                   service_url=activity.service_url)

        if self.reference is None or not isinstance(self.reference, ConversationReference):
            raise TypeError('BotContext.reference was not successfully created.'
                            ' An activity or conversation reference must be provided.')

    def reply_with_activity(self, activity: Activity) -> 'BotContext':
        BotAssert.activity_not_null(activity)
        self.responses.append(activity)
        return self

    def reply_with_text(self, text: str, speak: str=None) -> 'BotContext':
        reply: Activity = Activity(type=ActivityTypes.message,
                                   conversation=self.reference.conversation,
                                   service_url=self.reference.service_url,
                                   from_property=self.reference.bot,
                                   recipient=self.reference.user,
                                   text=text,
                                   id=str(uuid4()).replace('-',''))

        if speak and speak.replace(' ', ''):
            reply.speak = speak
        self.responses.append(reply)
        return self

    def set(self, object_id: str, service: object) -> None:
        if not object_id or not isinstance(object_id, str):
            raise TypeError('"object_id" must be a valid string.')
        self._services[object_id] = service

    def get(self, object_id: str) -> object:
        if not object_id or not isinstance(object_id, str):
            raise TypeError('"object_id" must be a valid with more than not string.')
        try:
            service = deepcopy(self._services[object_id])
            return service
        except BaseException:
            e = sys.exc_info()[0]
            raise e
