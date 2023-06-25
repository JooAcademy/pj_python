### 파이썬과 40개 작품들 
### 3장 4. QR코드 생성기2

import qrcode

file_path= "pythonStudy\\qr코드모음.txt" #파일 경로
#file_path= r'pythonStudy\qr코드모음.txt' #파일 경로 할 때 r을 붙여서 \를 하나만 적음
with open(file_path, "rt", encoding = "UTF8") as f:
    read_lines = f.readlines()

    for line in read_lines:
        line = line.strip() #줄바꿈 문자를 삭제
        print(line)



