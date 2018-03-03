# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from typing import List
from botbuilder.schema import Activity, ActivityTypes, ConversationReference

from .middleware import SendActivity
from ..bot_context import BotContext
from ..assertions import BotAssert


class BindOutgoingResponsesMiddleware(SendActivity):
    """
    Binds outgoing activities to a particular conversation.
    As messages are sent during the Send pipeline, they must be
    bound to the relevant ConversationReference object. This middleware
    runs at the start of the Sending Pipeline and binds all outgoing
    Activities to the ConversationReference on the Context.

    This Middleware component is automatically added to the Send Pipeline
    when constructing a bot.

    In terms of protocol level behavior, the binding of Activities to
    a ConversationReference is similar to how the Node SDK applies the same
    set of rules on all outbound Activities.
    """

    async def send_activity(self, context: BotContext, activities: List[Activity]) -> None:
        BotAssert.context_not_null(context)
        BotAssert.activity_list_not_null(activities)

        for activity in activities:
            if str(activity.type).replace(' ', '') or not activity.type:
                activity.type = ActivityTypes.message
            BindOutgoingResponsesMiddleware.apply_conversation_reference(activity, context.reference)

    @staticmethod
    def apply_conversation_reference(activity: Activity, reference: ConversationReference) -> None:
        """
        Applies all relevant Conversation related identifies to an activity. This effectively
        couples a blank Activity to a conversation.
        :param activity:
        :param reference:
        :return:
        """

        BotAssert.activity_not_null(activity)
        BotAssert.conversation_reference_not_null(reference)
        activity.channel_id = reference.channel_id
        activity.service_url = reference.service_url
        activity.conversation = reference.conversation
        activity.from_property = reference.bot
        activity.recipient = reference.user
        activity.reply_to_id = reference.activity_id
