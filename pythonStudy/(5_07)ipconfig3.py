### 파이썬과 40개 작품들 
### 3장 2. 내외부 IP알기

import socket
import requests
import re

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("www.google.co.kr", 443)) # 443포트는 https의 기본 접속 포트
print("내부IP:" , sock.getsockname()[0])

req = requests.get("http://ipconfig.kr")
out_addr = re.search(r"IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", req.text)[1]
print("외부IP:" , out_addr)










