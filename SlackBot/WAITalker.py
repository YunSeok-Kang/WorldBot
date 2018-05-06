import json
import requests

# JSON 데이터를 수신 후 가공하여 반환
def recv_wai_datas():
    r = requests.get('http://localhost:9994/Wai_interface.php'); # 링크는 외부 파일로 빼자.
    list_data = json.loads(r.text);

    return list_data;
