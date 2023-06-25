### 파이썬과 40개 작품들 
### 3장 6. 압축파일 암호 푸는 프로그램2


import itertools
import zipfile

passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
zfile = zipfile.ZipFile(r'pythonStudy\1234.zip')
for len in range(1, 6):
    to_attempt = itertools.product(passwd_string, repeat = len)
    for attempt in to_attempt:
        passwd = ''.join(attempt)
        print(passwd)
        try:
            zfile.extractall(pwd = passwd.encode())
            print(f"비빌번호는 {pwd} 입니다.")
            break
        except:
            pass




