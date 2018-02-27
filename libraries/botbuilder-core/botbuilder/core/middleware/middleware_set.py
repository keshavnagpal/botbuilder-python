# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.


import asyncio
from typing import Iterable, List

from .middleware import Middleware, ReceiveActivity, ContextCreated, SendActivity
from ..assertions import BotAssert
from ..bot_context import BotContext


class MiddlewareSet(ReceiveActivity, ContextCreated, SendActivity):
    """
    A set of `Middleware` plugins. The set itself is middleware so you can easily package up a set
    of middleware that can be composed into a bot with a single `bot.use(mySet)` call or even into
    another middleware set using `set.use(mySet)`.
    """
    def __init__(self):
        super(MiddlewareSet, self).__init__()
        self._middleware: List[Middleware] = []
        self._loop = asyncio.get_event_loop()

    def middleware(self):
        """
        Returns the underlying array of middleware.
        :return:
        """
        return self._middleware

    def use(self, *middleware: Iterable[Middleware]):
        """
        Registers middleware plugin(s) with the bot or set.
        :param middleware :
        :return:
        """
        BotAssert.middleware_set_not_null(middleware)
        self._middleware.extend(middleware)
        return self

    async def context_created(self, context):
        return await asyncio.ensure_future(self.__context_created(context, self._middleware))

    @staticmethod
    async def __context_created(context: BotContext, middleware_set: List[Middleware]):
        for middleware in middleware_set:
            if hasattr(middleware, 'context_created') and callable(middleware.context_created):
                await asyncio.ensure_future(middleware.context_created(context))

    async def receive_activity(self, context):
        return await asyncio.ensure_future(self.__receive_activity(context, self._middleware))

    async def receive_activity_with_status(self, context):
        return await asyncio.ensure_future(self.__receive_activity(context, self._middleware))

    @staticmethod
    async def __receive_activity(context, middleware_set):
        for middleware in middleware_set:
            if hasattr(middleware, 'receive_activity') and callable(middleware.receive_activity):
                await asyncio.ensure_future(middleware.receive_activity(context))

    async def send_activity(self, context, activities):
        return await asyncio.ensure_future(self.__send_activity(context, self._middleware, activities))

    async def __send_activity(self, context, middleware_set, activities):
        for middleware in middleware_set:
            if hasattr(middleware, 'send_activity') and callable(middleware.send_activity):
                await asyncio.ensure_future(middleware.send_activity(context, activities))
