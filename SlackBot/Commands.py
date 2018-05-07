from Services import WAI

services = []

# parameters
# msg_command: array of string.
#   idx [0]: service name
#   idx [1]: command
def find_command(msg_command):
    select_service(msg_command[0])
    if msg_command[1] == 'wai':
        print('')


def select_service(service_text):
    print('')

def test():
    print('test func')

services.append(WAI())
services[0].add_event('test', test())
services[0].run_event('test')