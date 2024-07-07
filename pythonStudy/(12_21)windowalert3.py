### ChatGPT 를 활용한 40가지 파이썬 프로그램 만들기
### 윈도우 알림 프로그램

# pip install pyttsx3
# pip install win10toast

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

import schedule
import time

def notify():
    # 알림 메시지
    message = "회의시작 10분전 입니다."
    
    # 알림 출력
    # toastlib 모듈 사용 예시
    # win10toast.ToastNotifier().show_toast("알림", message, duration=10)
    
    # 다른 알림 출력 방법 사용
    print(message)

# 일정 등록
schedule.every().monday.at("09:50").do(notify)
schedule.every().wednesday.at("09:50").do(notify)
schedule.every().tuesday.at("18:55").do(notify)
schedule.every().friday.at("09:50").do(notify)

while True:
    schedule.run_pending()
    time.sleep(1)