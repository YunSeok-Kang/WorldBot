import asyncio
import websockets
import json
import os
from slacker import Slacker

import Commands as cmds


class WorldBot:

    def __init__(self):
        self.m_token = os.environ["SLACK_BOT_TOKEN"]
        self.slack = Slacker(self.m_token)

        cmds.worldBot = self

        # members of SlackTalker
        self.websocket = None
        self.target_channel = ''
        self.target_user = ''
        # ...
        response = self.slack.rtm.start()

        if not response.successful:
            print("Connection Failed")
            return;

        self.bot_id = response.body['self'].get('id')
        self.sock_endpoint = response.body['url']

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        asyncio.get_event_loop().run_until_complete(self.execute_bot())
        asyncio.get_event_loop().run_forever()

    # parameters
    # message_json: message from slack. it must be a json type.
    def is_callme(self, message_json):

        if message_json.get('type') == 'message':
            # message_json.get('subtype') is None => 이슈 ID: 0000021
            #   edit, delete 등의 이벤트는 'subtype'으로 이벤트 정보가 넘어온다. None의 의미는 subtype이 아니란 말. 즉, 새로 전송된 메시지.
            if message_json.get('subtype') is None:
                # 명령어는 소문자로 변경하여 인식. 코딩의 편리성을 위해서.
                text_message = message_json.get('text').lower()
                if text_message.startswith('wb'):
                    return True

                else:
                    return False
            else:
                return False
        else:
            return False

    # def msg_recv(self, text):
    #   print(text)

    # json text를 가공하여 명령어 부분만 넘긴다.
    def command_parse(self, message):
        msg_arr = message.split(' ', 2)
        if len(msg_arr) <= 1:
            return False

        # 전처리 해주고(에러 잡기)
        # ex) 문자열이 '/WAI' 가 아니라, "/WAI"라고 들어오는 걸 하나로 통일하기 등.
        # 명령어를 모두 소문자로 바꾸는 기능도 넣자. 소문자만 비교해도 되도록.
        # 그 후에...
        return msg_arr[1:]

    async def execute_bot(self):
        self.websocket = await websockets.connect(self.sock_endpoint)
        while True:
            message_json = await self.websocket.recv()
            message_json = json.loads(message_json)
            if self.is_callme(message_json):  # Write something if users call you(Bot)

                # 임시 방편. 봇을 언급한 메시지가 날아오면 해당 json 내의 channel과 user로 데이터를 업데이트 해놓음.
                # slack으로 데이터를 보내는데에 사용됨.
                self.target_channel = message_json.get('channel')
                self.target_user = message_json.get('user')

                # ...

                # Is a command? if yes...
                parsed_command = self.command_parse(message_json.get('text').lower())
                if parsed_command:
                    cmds.find_command(parsed_command)

    def msg_to_slack(self, text, attachments=None):
        self.slack.chat.post_message(channel='#general', text='', attachments=attachments, username='worldbot_test')
        #self.slack.chat.post_message(channel='#development_test', text='test', username='worldbot_test')

if __name__ == "__main__":
    worldBot = WorldBot();
