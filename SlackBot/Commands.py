from Services import Service
from Services import WAI

# Target WorldBot
worldBot = None

# List of services
services = []


def init():
    Service.target_world_bot = worldBot

    services.append(WAI())
    services[0].add_event('info', services[0].info)
    services[0].add_event('add', services[0].add_service)

# parameters
# msg_command: array of string.
#   idx [0]: service name
#   idx [1]: command
def find_command(msg_command):
    print(msg_command)
    target = select_service(msg_command[0])
    if target:
        if len(msg_command) < 3:
            target.run_event(msg_command[1])
        else:
            target.run_event(msg_command[1], msg_command[2])
    else:
        print('명령어를 찾지 못했습니다.')


def select_service(service_text):
    if service_text == 'wai':
        return services[0]
    else:
        print('존재하지 않는 서비스입니다.')