> 아직 배포할 생각 없어서 혼자만 알아볼 수 있게 짜놓음. 첫 파이썬 프로젝트라 엉망.

추가 설치된 패키지

slacker, websockets, requests

# 구성
- WorldBot.py
- SlackTalker.py
    - Commands.py
- WAITalker.py

# 개발 상태
현재는 WorldBot내에 SlackTalker에서 해야할 기능을 구현해놨다. 직접 메시지를 받아버리는 상태. 하지만 슬랙과 통신하는 부분은 모두 뺄 생각.

Commands에 있는 세부 명령은 현재 동작하지 않는 상태. /WAI 만 가능.
 
WorldBot에 있는 msg_to_slack 함수 수정해야함. sockets의 send 기능을 통해 json으로 데이터를 정확히 전송하는 법을 알아내거나, slacker의 채팅 기능으로 전송할 수 있게 channel의 id를 기반으로 name을 유추하는 방법을 알아내거나... 제 3의 방법이 있으려나?     
# 아이디어
SlackTalker에서 비동기식으로 데이터를 받아들이고, 데이터가 도착하면 가공 후 WorldBot에게 이벤트를 발생시키는건 어떨지?
asyncio에 대해서 공부해보자.

# Commands
**사용법**
> /명령어 세부명령




