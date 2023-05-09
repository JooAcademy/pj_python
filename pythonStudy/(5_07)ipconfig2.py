### 파이썬과 40개 작품들 
### 3장 2. 외부 IP알기

import requests
import re

'''
print(requests.get("http://ip.jsontest.com").json()["ip"])
'''


req = requests.get("http://ipconfig.kr")
out_addr = re.search(r"IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", req.text)[1]
print(out_addr)










