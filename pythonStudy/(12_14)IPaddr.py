### ChatGPT 를 활용한 40가지 파이썬 프로그램 만들기
###  외부 / 내부 IP 확인
'''
1숫자맞추기 게임/2컴퓨터내외부 IP/3텍스트음성변환/4QR코드생성기/5컴퓨터정보확인
6압축암호풀기/7환율변환기/8파일압축하기/9영어문서한글번역/10이메일수집엑셀저장
11엑셀에서자동이멜발송/12가짜개인정보엑셀저장/13단위변환기/14실시간주가조회/15알림프로그램
16맞춤법검사기/17날씨예보/18음악재생프로그램/19패스워드생성기/20오늘의명언프로그램
21인터넷라디오스트리밍/22MBTI성격검사/23날짜계산기/24가상화폐표시/25가상화폐데이터저장
26데이터베이스 데이터 읽어 그래프그리기/27로또번호/28컴퓨터예약종료/29음식추천/30단어암기
31자동백업/32이미지에서글자추출OCR/33사진얼굴모자이크/34플라스크사진서버/35플라스크게시판
36플라스크투표/37음성인식비서/38인공지능챗봇/39자연어처리/40머신러닝
'''

import socket
import requests

# 호스트 이름 얻기
host_name = socket.gethostname()

# 호스트 IP 주소 얻기
host_ip = socket.gethostbyname(host_name)

# 외부 IP 주소를 가져오는 API 주소
api_url = "https://api.ipify.org"

# API 요청 보내기
response = requests.get(api_url)

# 외부 IP 주소 얻기
external_ip = response.text

print("호스트 이름: ", host_name)
print("호스트 IP 주소: ", host_ip)
print("외부 IP 주소: ", external_ip)