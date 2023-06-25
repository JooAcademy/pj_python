### 파이썬과 40개 작품들 
### 3장 4. QR코드 생성기

import qrcode

qr_data = "www.naver.com"
qr_img = qrcode.make(qr_data)

save_path = "pythonStudy\\" + qr_data + ".png"  # 디렉토리 경로 + 네이버주소 + 이미지확장자
qr_img.save(save_path)


