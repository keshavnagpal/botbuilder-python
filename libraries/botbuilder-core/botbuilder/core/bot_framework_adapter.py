# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import asyncio
from typing import List, Callable
from botbuilder.schema import Activity, ActivityTypes
from botframework.connector import ConnectorClient
from botframework.connector.auth import (MicrosoftAppCredentials,
                                         JwtTokenValidation, SimpleCredentialProvider)

from .bot_adapter import BotAdapter
from .assertions import BotAssert
from .bot_context import BotContext
from .middleware import Middleware


class BotFrameworkAdapter(BotAdapter):

    def __init__(self, app_id: str, app_password: str):
        super(BotFrameworkAdapter, self).__init__()
        self._credentials = MicrosoftAppCredentials(app_id, app_password)
        self._credential_provider = SimpleCredentialProvider(app_id, app_password)
        self.on_receive: Callable[[BotContext], None] = None

    def use(self, middleware: Middleware):
        self._middleware_set.use(middleware)
        return self

    async def process_activity(self, auth_header: str, activity: Activity, callback):
        BotAssert.activity_not_null(activity)
        await JwtTokenValidation.assert_valid_activity(activity, auth_header, self._credential_provider)

        context = BotContext(self, activity)
        await self.run_pipeline(context, callback)

    def send(self, activities: List[Activity]):
        for activity in activities:
            connector = ConnectorClient(self._credentials, base_url=activity.service_url)
            connector.conversations.send_to_conversation(activity.conversation.id, activity)

    def receive(self, auth_header: str, activity: Activity):
        loop = asyncio.new_event_loop()
        try:
            loop.run_until_complete(JwtTokenValidation.assert_valid_activity(
                activity, auth_header, self._credential_provider))
        finally:
            loop.close()
        if self.on_receive is not None:
            self.on_receive(activity)

    async def send_activities_implementation(self, context: BotContext, activities: List[Activity]):
        for activity in activities:
            # if activity and activity.type == ActivityTypes.delay.value:
            #     pass
            #     # sleep or something for activity.value
            # else:
            #     connector_client = ConnectorClient(self._credentials, activity.service_url)
            #     connector_client.conversations.send_to_conversation(activity.conversation.id, activity)
            connector_client = ConnectorClient(self._credentials, activity.service_url)
            connector_client.conversations.send_to_conversation(activity.conversation.id, activity)

    def update_activity_implementation(self, context: BotContext, activity: Activity):
        try:
            connector_client = ConnectorClient(self._credentials, activity.service_url)
            reference = context.conversation_reference()
            return connector_client.conversations.update_activity(reference.id, reference.activity_id, activity)
        except BaseException:
            raise BaseException()

    def delete_activity_implementation(self, context: BotContext, conversation_id: str, activity_id: str):
        try:
            request: Activity = context.request()
            connector_client = ConnectorClient(self._credentials, request.service_url)
            connector_client.conversations.delete_activity(request.conversation.id, request.id)
        except BaseException:
            raise BaseException()

    async def create_conversation_implementation(self):
        raise NotImplementedError()
