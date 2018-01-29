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


class Activity(Model):
    """An Activity is the basic communication type for the Bot Framework 3.0
    protocol.

    :param type: The type of the activity. Possible values include: 'message',
     'contactRelationUpdate', 'conversationUpdate', 'typing', 'ping',
     'endOfConversation', 'event', 'invoke', 'deleteUserData', 'messageUpdate',
     'messageDelete', 'installationUpdate', 'messageReaction', 'suggestion'
    :type type: str or ~bot.connector.models.ActivityTypes
    :param id: ID of this activity
    :type id: str
    :param timestamp: UTC Time when message was sent (set by service)
    :type timestamp: datetime
    :param local_timestamp: Local time when message was sent (set by client,
     Ex: 2016-09-23T13:07:49.4714686-07:00)
    :type local_timestamp: datetime
    :param service_url: Service endpoint where operations concerning the
     activity may be performed
    :type service_url: str
    :param channel_id: ID of the channel where the activity was sent
    :type channel_id: str
    :param from_property: Sender address
    :type from_property: ~bot.connector.models.ChannelAccount
    :param conversation: Conversation
    :type conversation: ~bot.connector.models.ConversationAccount
    :param recipient: (Outbound to bot only) Bot's address that received the
     message
    :type recipient: ~bot.connector.models.ChannelAccount
    :param text_format: Format of text fields Default:markdown. Possible
     values include: 'markdown', 'plain', 'xml'
    :type text_format: str or ~bot.connector.models.TextFormatTypes
    :param attachment_layout: Hint for how to deal with multiple attachments.
     Default:list. Possible values include: 'list', 'carousel'
    :type attachment_layout: str or
     ~bot.connector.models.AttachmentLayoutTypes
    :param members_added: Members added to the conversation
    :type members_added: list[~bot.connector.models.ChannelAccount]
    :param members_removed: Members removed from the conversation
    :type members_removed: list[~bot.connector.models.ChannelAccount]
    :param reactions_added: Reactions added to the activity
    :type reactions_added: list[~bot.connector.models.MessageReaction]
    :param reactions_removed: Reactions removed from the activity
    :type reactions_removed: list[~bot.connector.models.MessageReaction]
    :param topic_name: The conversation's updated topic name
    :type topic_name: str
    :param history_disclosed: True if prior history of the channel is
     disclosed
    :type history_disclosed: bool
    :param locale: The language code of the Text field
    :type locale: str
    :param text: Content for the message
    :type text: str
    :param speak: SSML Speak for TTS audio response
    :type speak: str
    :param input_hint: Input hint to the channel on what the bot is expecting.
     Possible values include: 'acceptingInput', 'ignoringInput',
     'expectingInput'
    :type input_hint: str or ~bot.connector.models.InputHints
    :param summary: Text to display if the channel cannot render cards
    :type summary: str
    :param suggested_actions: SuggestedActions are used to provide
     keyboard/quickreply like behavior in many clients
    :type suggested_actions: ~bot.connector.models.SuggestedActions
    :param attachments: Attachments
    :type attachments: list[~bot.connector.models.Attachment]
    :param entities: Collection of Entity objects, each of which contains
     metadata about this activity. Each Entity object is typed.
    :type entities: list[~bot.connector.models.Entity]
    :param channel_data: Channel-specific payload
    :type channel_data: object
    :param action: ContactAdded/Removed action
    :type action: str
    :param reply_to_id: The original ID this message is a response to
    :type reply_to_id: str
    :param value: Open-ended value
    :type value: object
    :param name: Name of the operation to invoke or the name of the event
    :type name: str
    :param relates_to: Reference to another conversation or activity
    :type relates_to: ~bot.connector.models.ConversationReference
    :param code: Code indicating why the conversation has ended. Possible
     values include: 'unknown', 'completedSuccessfully', 'userCancelled',
     'botTimedOut', 'botIssuedInvalidMessage', 'channelFailed'
    :type code: str or ~bot.connector.models.EndOfConversationCodes
    :param expiration: DateTime to expire the activity as ISO 8601 encoded
     datetime
    :type expiration: datetime
    :param importance: Importance of this activity
     {Low|Normal|High}, null value indicates Normal importance see
     ActivityImportance)
    :type importance: str
    :param delivery_mode: Hint to describe how this activity should be
     delivered.
     Currently: null or "Default" = default delivery
     "Notification" = notification semantics
    :type delivery_mode: str
    :param text_highlights: TextHighlight in the activity represented in the
     ReplyToId property
    :type text_highlights: list[~bot.connector.models.TextHighlight]
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'},
        'local_timestamp': {'key': 'localTimestamp', 'type': 'iso-8601'},
        'service_url': {'key': 'serviceUrl', 'type': 'str'},
        'channel_id': {'key': 'channelId', 'type': 'str'},
        'from_property': {'key': 'from', 'type': 'ChannelAccount'},
        'conversation': {'key': 'conversation', 'type': 'ConversationAccount'},
        'recipient': {'key': 'recipient', 'type': 'ChannelAccount'},
        'text_format': {'key': 'textFormat', 'type': 'str'},
        'attachment_layout': {'key': 'attachmentLayout', 'type': 'str'},
        'members_added': {'key': 'membersAdded', 'type': '[ChannelAccount]'},
        'members_removed': {'key': 'membersRemoved', 'type': '[ChannelAccount]'},
        'reactions_added': {'key': 'reactionsAdded', 'type': '[MessageReaction]'},
        'reactions_removed': {'key': 'reactionsRemoved', 'type': '[MessageReaction]'},
        'topic_name': {'key': 'topicName', 'type': 'str'},
        'history_disclosed': {'key': 'historyDisclosed', 'type': 'bool'},
        'locale': {'key': 'locale', 'type': 'str'},
        'text': {'key': 'text', 'type': 'str'},
        'speak': {'key': 'speak', 'type': 'str'},
        'input_hint': {'key': 'inputHint', 'type': 'str'},
        'summary': {'key': 'summary', 'type': 'str'},
        'suggested_actions': {'key': 'suggestedActions', 'type': 'SuggestedActions'},
        'attachments': {'key': 'attachments', 'type': '[Attachment]'},
        'entities': {'key': 'entities', 'type': '[Entity]'},
        'channel_data': {'key': 'channelData', 'type': 'object'},
        'action': {'key': 'action', 'type': 'str'},
        'reply_to_id': {'key': 'replyToId', 'type': 'str'},
        'value': {'key': 'value', 'type': 'object'},
        'name': {'key': 'name', 'type': 'str'},
        'relates_to': {'key': 'relatesTo', 'type': 'ConversationReference'},
        'code': {'key': 'code', 'type': 'str'},
        'expiration': {'key': 'expiration', 'type': 'iso-8601'},
        'importance': {'key': 'importance', 'type': 'str'},
        'delivery_mode': {'key': 'deliveryMode', 'type': 'str'},
        'text_highlights': {'key': 'textHighlights', 'type': '[TextHighlight]'},
    }

    def __init__(self, type=None, id=None, timestamp=None, local_timestamp=None, service_url=None, channel_id=None, from_property=None, conversation=None, recipient=None, text_format=None, attachment_layout=None, members_added=None, members_removed=None, reactions_added=None, reactions_removed=None, topic_name=None, history_disclosed=None, locale=None, text=None, speak=None, input_hint=None, summary=None, suggested_actions=None, attachments=None, entities=None, channel_data=None, action=None, reply_to_id=None, value=None, name=None, relates_to=None, code=None, expiration=None, importance=None, delivery_mode=None, text_highlights=None):
        super(Activity, self).__init__()
        self.type = type
        self.id = id
        self.timestamp = timestamp
        self.local_timestamp = local_timestamp
        self.service_url = service_url
        self.channel_id = channel_id
        self.from_property = from_property
        self.conversation = conversation
        self.recipient = recipient
        self.text_format = text_format
        self.attachment_layout = attachment_layout
        self.members_added = members_added
        self.members_removed = members_removed
        self.reactions_added = reactions_added
        self.reactions_removed = reactions_removed
        self.topic_name = topic_name
        self.history_disclosed = history_disclosed
        self.locale = locale
        self.text = text
        self.speak = speak
        self.input_hint = input_hint
        self.summary = summary
        self.suggested_actions = suggested_actions
        self.attachments = attachments
        self.entities = entities
        self.channel_data = channel_data
        self.action = action
        self.reply_to_id = reply_to_id
        self.value = value
        self.name = name
        self.relates_to = relates_to
        self.code = code
        self.expiration = expiration
        self.importance = importance
        self.delivery_mode = delivery_mode
        self.text_highlights = text_highlights
