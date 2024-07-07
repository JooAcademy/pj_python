### ChatGPT 를 활용한 40가지 파이썬 프로그램 만들기
### 실시간 주가 조회 프로그램

# pip install beautifulsoup4
# pip install pandas


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

#url = f'https://finance.naver.com/sise/sise_market_sum.naver'
url = f'https://finance.naver.com/sise/sise_market_sum.naver?&page=2'



res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')


'''
stock_name2 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(2) > td:nth-child(2) > a')
print(stock_name2.text)

current_price2 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(2) > td:nth-child(3)')
print(current_price2.text)

'''


for i in range(2, 70):
    stock_name = soup.select_one(f"#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child({i}) > td:nth-child(2) > a")
    if stock_name is not None:
        current_price = soup.select_one(f"#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child({i}) > td:nth-child(3)")
        print(f"{stock_name.text} 현재가: {current_price.text}")
      
