# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import sys
import http.server
import json
import asyncio
from botbuilder.schema import (Activity, ActivityTypes)
from botbuilder.core import *
from botbuilder.core.middleware import ContextCreated, ReceiveActivity, SendActivity

APP_ID = ''
APP_PASSWORD = ''


class MyContextCreatedMiddleware(ContextCreated):
    async def context_created(self, context):
        print('Received the context, MyContextCreatedMiddleware.context_created() has been run!')


class MyReceiveActivityMiddleware(ReceiveActivity):
    async def receive_activity(self, context):
        print('Received the activity, MyReceiveActivityMiddleware.receive_activity() has been run!')


class MySendActivityMiddleware(SendActivity):
    async def send_activity(self, context, activities):
        if context.request.type == ActivityTypes.conversation_update.value:
            if context.request.members_added[0].id != context.request.recipient.id:
                context.reply('Welcome to the the echo bot!')


bot = BotFrameworkAdapter(APP_ID, APP_PASSWORD)
bot.register_middleware(MyContextCreatedMiddleware())
bot.register_middleware(MyReceiveActivityMiddleware())


class BotRequestHandler(http.server.BaseHTTPRequestHandler):
    bot: BotFrameworkAdapter = bot
    __loop = asyncio.get_event_loop()

    @staticmethod
    def __create_reply_activity(request_activity, text):
        return Activity(
            type=ActivityTypes.message,
            channel_id=request_activity.channel_id,
            conversation=request_activity.conversation,
            recipient=request_activity.from_property,
            from_property=request_activity.recipient,
            text=text,
            service_url=request_activity.service_url)

    @staticmethod
    def __create_delay_activity(request_activity, delay_ms):
        return Activity(
            type='delay',
            value=delay_ms,
            channel_id=request_activity.channel_id,
            conversation=request_activity.conversation,
            recipient=request_activity.from_property,
            from_property=request_activity.recipient,
            service_url=request_activity.service_url)

    def do_POST(self):
        body = self.rfile.read(int(self.headers['Content-Length']))
        data = json.loads(str(body, 'utf-8'))
        activity = Activity.deserialize(data)
        if activity.type != ActivityTypes.conversation_update.value:
            try:
                if self.__loop.is_running():
                    asyncio.ensure_future(self.bot.process_activity(
                        self.headers['Authorization'] or '', activity, self.response_handler))
                else:
                    self.__loop.run_until_complete(self.bot.process_activity(
                        self.headers['Authorization'] or '', activity, self.response_handler))
            except Exception:
                exce = sys.exc_info()[0]
                print(exce)
                self.send_response(500)
                self.end_headers()
        else:
            self.send_response(200)
            self.end_headers()

    async def response_handler(self, context):
        reply = self.__create_reply_activity(context.request, 'You said, "%s".' % context.request.text)
        delay = self.__create_delay_activity(context.request, 2000)
        context.reply_with_activity(delay).reply_with_activity(reply)
        context.reply_with_activity(delay)
        context.reply_with_text('Hello!')

        self.send_response(202)
        self.end_headers()

    def __unhandled_activity(self):
        self.send_response(404)
        self.end_headers()

    def do_GET(self):
        self.__unhandled_activity()


try:
    SERVER = http.server.HTTPServer(('localhost', 9000), BotRequestHandler)
    print('Started http server on port 9000.')
    SERVER.serve_forever()
except KeyboardInterrupt:
    print('^C received, shutting down server')
    SERVER.socket.close()
