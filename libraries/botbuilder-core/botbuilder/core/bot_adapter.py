# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import asyncio
from abc import ABC, abstractmethod
from typing import List
from botbuilder.schema import Activity, ConversationReference

# from .assertions import BotAssert
from .bot_context import BotContext
from .middleware import Middleware, MiddlewareSet, BindOutgoingResponsesMiddleware, TemplateManager


class BotAdapter(ABC):
    def __init__(self):
        self._middleware_set = MiddlewareSet()
        # self.register_middleware(BindOutgoingResponsesMiddleware())
        # self.register_middleware(TemplateManager())
        self._loop = asyncio.get_event_loop()

    def register_middleware(self, middleware: Middleware):
        self._middleware_set.use(middleware)

    @abstractmethod
    async def send_activities_implementation(self, context: BotContext, activities: List[Activity]): pass

    @abstractmethod
    async def update_activity_implementation(self, context: BotContext, activity: Activity): pass

    @abstractmethod
    async def delete_activity_implementation(self, context: BotContext, conversation_id: str, activity_id: str): pass

    @abstractmethod
    async def create_conversation_implementation(self): pass

    async def run_pipeline(self, context: BotContext, callback=None):
        # BotAssert.context_not_null(context)

        # print('Middleware: beginning pipeline for %s' % context.conversation_reference.activity_id)
        if self._loop.is_running():
            await asyncio.ensure_future(self._middleware_set.context_created(context))

            if context.request:
                did_all_middleware_run = asyncio.ensure_future(self._middleware_set.receive_activity_with_status(context))
                if did_all_middleware_run and callback and callable(callback):
                    asyncio.ensure_future(callback(context))
                else:
                    pass
            else:
                if callback and callable(callback):
                    asyncio.ensure_future(callback(context))
            await asyncio.ensure_future(self._middleware_set.send_activity(context, context.responses or []))
            if context.responses:
               await asyncio.ensure_future(self.send_activities_implementation(context, context.responses))
        else:
            self._loop.run_until_complete(asyncio.ensure_future(self._middleware_set.context_created(context)))

            if context.request:
                did_all_middleware_run = self._loop.run_until_complete(asyncio.ensure_future(
                    self._middleware_set.receive_activity_with_status(context)))
                if did_all_middleware_run and callback and callable(callback):
                    self._loop.run_until_complete(asyncio.ensure_future(callback(context)))
                else:
                    pass
            else:
                if callback and callable(callback):
                    self._loop.run_until_complete(asyncio.ensure_future(callback(context)))
            self._loop.run_until_complete(asyncio.ensure_future(self._middleware_set.send_activity(context, context.responses or [])))
            if context.responses:
                self._loop.run_until_complete(asyncio.ensure_future(self.send_activities_implementation(context, context.responses)))

        # print('Middleware: Ending Pipeline for %s' % context.conversation_reference.activity_id

    async def continue_conversation(self, reference: ConversationReference, callback):
        context = BotContext(self, reference=reference)
        await self.run_pipeline(context, callback)

    async def create_conversation(self, channel_id: str, callback):
        raise NotImplementedError()
