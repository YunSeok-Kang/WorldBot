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

# parameters
# msg_command: array of string.
#   idx [0]: service name
#   idx [1]: command
def find_command(msg_command):
    target = select_service(msg_command[0])
    if target:
        target.run_event(msg_command[1], 'obj')


def select_service(service_text):
    if service_text == 'wai':
        return services[0]
    else:
        print('존재하지 않는 서비스입니다.')