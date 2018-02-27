# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from typing import List
from botbuilder.schema import Activity, ConversationReference

# from .bot_adapter import BotAdapter  #BotAdapter shouldn't depend on Context and vice versa, otherwise, import errors.


class BotContext(object):
    def __init__(self, adapter, activity: Activity=None, reference: ConversationReference=None):
        self._adapter = adapter
        self.conversation_reference = reference
        self.request = activity
        self.responses: List[Activity] = []

        if activity is not None:
            pass
        if reference is not None:
            pass

    def reply(self, text: str=None, speak: str=None, activity: Activity=None) -> 'BotContext':
        if not text and not activity:
            raise TypeError('Responses to send with BotContext.reply not found.'
                            'You must provide either text or activities')
        if text and not activity:
            reply = self.conversation_reference()  #.get_post_to_user_message()???
            reply.text = text
            if speak and speak.strip():
                reply.speak = speak
            self.responses.append(reply)
        elif activity:
            # BotAssert.activity_not_null(activity)
            self.responses.append(activity)
        return self

