# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from abc import ABC, abstractmethod
from typing import List
from botbuilder.schema import Activity

from ..bot_context import BotContext


class Middleware(ABC):
    pass


class ContextCreated(Middleware):
    @abstractmethod
    async def context_created(self, context): pass


class ReceiveActivity(Middleware):
    @abstractmethod
    async def receive_activity(self, context: BotContext): pass


class SendActivity(Middleware):
    @abstractmethod
    async def send_activity(self, context: BotContext, activities: List[Activity]): pass


class AnonymousReceiveMiddleware(ReceiveActivity):
    def __init__(self, to_call):
        if not to_call and not callable(to_call):
            raise TypeError('"to_call" must be provided and be callable.')
        self._to_call = to_call

    def receive_activity(self, context: BotContext):
        return self._to_call(context)


class AnonymousContextCreatedMiddleware(ContextCreated):
    def __init__(self, to_call):
        if not to_call and not callable(to_call):
            raise TypeError('"to_call" must be provided and be callable.')
        self._to_call = to_call

    def context_created(self, context):
        return self._to_call(context)


class AnonymousSendActivityMiddleware(SendActivity):
    def __init__(self, to_call):
        if not to_call and not callable(to_call):
            raise TypeError('"to_call" must be provided and be callable.')
        self._to_call = to_call

    def send_activity(self, context: BotContext, activities: List[Activity]):
        return self._to_call(context, activities)
