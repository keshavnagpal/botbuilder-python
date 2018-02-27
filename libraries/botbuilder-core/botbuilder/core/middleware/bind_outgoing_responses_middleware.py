# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from typing import List
from botbuilder.schema import Activity

from .middleware import SendActivity
from ..bot_context import BotContext


class BindOutgoingResponsesMiddleware(SendActivity):
    async def send_activity(self, context: BotContext, activities: List[Activity]):
        raise NotImplementedError()
