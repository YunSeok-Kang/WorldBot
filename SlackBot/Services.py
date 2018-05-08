import WAITalker

class Service:
    target_world_bot = None

    def __init__(self):
        # 이를 자식 클래스에서 실행시킬 방법은?

        # 멤버 변수
        self.events = dict()

        # 서비스 이름. 소문자로 적어야 함.
        self.service_name = ''
        # ...

    def add_event(self, event_name, event_action):
        self.events[event_name] = event_action

    def run_event(self, event_name, param=None):
        if event_name in self.events:
            action = self.events[event_name]
            if param:
                action(param)
            else:
                action()

class WAI(Service):

    def __init__(self):
        Service.__init__(self)
        self.service_name = 'wai'

    def info(self, obj):
        if obj:
            print('here is a obj')

        attachments_dict = dict()

        msg = ''
        for wai_data in WAITalker.recv_wai_datas():
            msg += wai_data['name'] + '\n http://' + wai_data['ip'] + ':' + wai_data['port'] + '\n'

        attachments_dict['title'] = 'World Applications Info'
        attachments_dict['text'] = msg

        if Service.target_world_bot:
            Service.target_world_bot.msg_to_slack(text=' ', attachments=[attachments_dict])
        else:
            print('Services.py: Service.target_world_bot에 데이터가 존재하지 않습니다.')