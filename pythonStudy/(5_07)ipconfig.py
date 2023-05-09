### 파이썬과 40개 작품들 
### 3장 2. 내부 IP알기

import socket

'''
# 내부 IP 알아보기
    in_addr = socket.gethostbyname(socket.gethostname())
    print(in_addr)
'''

'''
# 외부 사이트 접속을 통해서 내부 IP 알아보기
'''
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("www.google.co.kr", 443)) # 443포트는 https의 기본 접속 포트
print(sock.getsockname()[0])













