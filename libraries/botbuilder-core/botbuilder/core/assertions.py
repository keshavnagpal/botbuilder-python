# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from typing import Iterable
from botbuilder.schema import Activity, ConversationReference

# from .bot_context import BotContext
# from .middleware import Middleware


class BotAssert(object):

    @staticmethod
    def activity_not_null(activity: Activity):
        if not activity:
            raise TypeError()

    @staticmethod
    def context_not_null(context):# BotContext):
        if not context:
            raise TypeError()

    @staticmethod
    def conversation_reference_not_null(reference: ConversationReference):
        if not reference:
            raise TypeError()

    @staticmethod
    def adapter_not_null(adapter):
        if not adapter:
            raise TypeError()

    @staticmethod
    def activity_list_not_null(activity_list: Iterable[Activity]):
        if not activity_list:
            raise TypeError()

    @staticmethod
    def middleware_not_null(middleware):# Middleware):
        if not middleware:
            raise TypeError()

    @staticmethod
    def middleware_set_not_null(middleware):# Iterable[Middleware]):
        if not middleware:
            raise TypeError()
