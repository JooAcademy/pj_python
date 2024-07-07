### ChatGPT 를 활용한 40가지 파이썬 프로그램 만들기
### 환율 변환기


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

import requests

def currency_converter(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    exchange_rate = data['rates'][to_currency]
    result = round(amount * exchange_rate, 2)
    return result

while True:
    try:
        amount = float(input("변환하려는 금액을 입력하세요:"))
        from_currency = input("어떤 화폐에서 변환하시겠습니까? (예: USD, KRW):").upper()
        to_currency =  input("어떤 화폐로 변환하시겠습니까? (예: USD, KRW):").upper()
        result = currency_converter(amount, from_currency, to_currency)
        print(f"{amount}{from_currency}은(는) {result}{to_currency}입니다. ")100
        choice = input("계속 변환하시겠습니까? (Y/N):").upper()
        if choice != "Y":
            break
    except:
        print("올바른 값을 입력하여 주세요")
