import json
import requests

# JSON 데이터를 수신 후 가공하여 반환
def recv_wai_datas():
    args = {'command': 'info'}

    r = requests.get('http://localhost:9994/Wai_interface.php', args); # 링크는 외부 파일로 빼자.
    list_data = json.loads(r.text);

    return list_data;

def add_wai_service(name, hosting_server, port, domain=None):
    args = {'command':'add', 'name': name, 'domain':domain, 'hosting_server':hosting_server, 'port':port}


    # hosting_server가 hosting_info_table에 존재하는 녀석인지 확인할 필요가 있음.
    # 사용 중인 포트인지도 확인 필요.
    # name이 이미 존재하는 것인지도 확인 필요.

    r = requests.get('http://13.124.168.174:9994/Wai_interface.php', args)

    return json.loads(r.text)

'''
if __name__ == "__main__":
    # recv_wai_datas();
    # add_wai_service('TEST', '')

    # None 데이터는 PHP에서 null으로 인식되는 것으로 확인.
    args = {'command': 'info', 'test': None}
    r = requests.get('http://13.124.168.174:9994/Wai_interface.php', args)
    print(r.text)
'''