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

    def send_msg_to_bot(self, text, attachments=None):
        if Service.target_world_bot:
            Service.target_world_bot.msg_to_slack(text=' ', attachments=attachments)
        else:
            print('Services.py: Service.target_world_bot에 데이터가 존재하지 않습니다.')


class WAI(Service):

    def __init__(self):
        Service.__init__(self)
        self.service_name = 'wai'

    # Todo: domain이 null이 아니면 domain을 보여주고, domain이 null이면 ip를 보여주도록 수정하자.
    def info(self):
        attachments_dict = dict()

        msg = ''
        for wai_data in WAITalker.recv_wai_datas():
            msg += wai_data['name'] + '\n http://' + wai_data['ip'] + ':' + wai_data['port'] + '\n'

        attachments_dict['title'] = 'World Applications Info'
        attachments_dict['text'] = msg

        self.send_msg_to_bot(' ', [attachments_dict])


    def add_service(self, param):
        attachments_dict = dict()

        if (param == '' or param == None):
            attachments_dict['title'] = '서비스 등록 오류.'
            attachments_dict['text'] = '명령어 형식을 확인하세요. \n 형식: wb wai add 서비스명'
        else:
            attachments_dict['title'] = param + ' 서비스 등록을 시작합니다.'
            attachments_dict['text'] = '아직 완성되지 않았습니다. slack에서 명령어로 등록을 완료할지, 등록 페이지 url을 넘길지 고민 중입니다.'

        # WAITalker.add_wai_service 실행시켜야 함.

        self.send_msg_to_bot(' ', [attachments_dict])

        print(param)