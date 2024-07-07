### ChatGPT 를 활용한 40가지 파이썬 프로그램 만들기
### 이메일 주소 수집하기

# pip install beautifulsoup4
# pip install pandas
# pip install --upgrade pip

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
import requests  # 웹페이지에서 데이터를 가져오는 모듈
from bs4 import BeautifulSoup  # HTML 파싱을 위한 모듈
import re  # 정규표현식을 위한 모듈
import pandas as pd  # 데이터 분석 및 엑셀 파일 저장을 위한 모듈

# 웹페이지의 URL
url = "https://v.daum.net/v/20230303140011566"

# requests 모듈을 이용하여 웹페이지의 HTML 코드를 가져옴
response = requests.get(url)

# BeautifulSoup 모듈을 이용하여 HTML 코드를 파싱
soup = BeautifulSoup(response.text, "html.parser")

# 이메일 패턴
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+[A-Za-z]{2,}\b'

# 웹페이지에서 찾은 이메일 리스트
emails = []

# HTML 코드의 텍스트를 가져옴
text = soup.get_text()

# 정규표현식을 이용하여 이메일을 찾음
for match in re.findall(email_pattern, text):
    emails.append(match)

# 중복된 이메일 제거
emails = list(set(emails))

# 찾은 이메일 리스트를 DataFrame으로 변환
df = pd.DataFrame(emails, columns=['Email'])

# 엑셀 파일로 저장
df.to_excel('JooAcademy/pythonStudy/emailtoexcel.xlsx', index=False)