import WAITalker

worldBot = None

# parameters
# msg_command: array of string.
#   idx [0]: command type
#   idx [1]: details of command
def find_command(msg_command):
    if msg_command[0] == 'wai':
        cmd_callwai()


def cmd_callwai():

    attachments_dict = dict()

    msg = ''
    for wai_data in WAITalker.recv_wai_datas():
        msg += wai_data['name'] + '\n http://' + wai_data['ip'] + ':' + wai_data['port'] + '\n'

    attachments_dict['title'] = 'World Applications Info';
    attachments_dict['text'] = msg;

    worldBot.msg_to_slack(text= ' ', attachments=[attachments_dict])

    #worldBot.msg_to_slack('#development_test', 'WorldBot', 'Test')
