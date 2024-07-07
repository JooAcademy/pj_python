### ChatGPT 를 활용한 40가지 파이썬 프로그램 만들기
### 컴퓨터 예약 종료 프로그램


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

from tkinter import *
import os

def shutdown_computer():
    '''컴퓨터를 예약 종료하는 함수'''
    # 사용자로부터 종료 시간 입력 받기
    minutes = int(minutes_entry.get())
    
    # 시스템 명령어를 실행하여 컴퓨터 종료
    os.system(f'shutdown -s -t {minutes * 60}')

def cancel_shutdown():
    '''예약 종료를 취소하는 함수'''
    # 시스템 명령어를 실행하여 예약 종료 취소
    os.system('shutdown -a')

# GUI 생성
window = Tk()
window.title("컴퓨터 예약 종료")
window.geometry("300x200")

# 종료 시간 입력 필드 생성
minutes_label = Label(window, text="종료 시간 (분):")
minutes_label.grid(row=0, column=0)
minutes_entry = Entry(window)
minutes_entry.grid(row=0, column=1)

# 종료 버튼 생성
shutdown_button = Button(window, text="종료", command=shutdown_computer)
shutdown_button.grid(row=1, column=0)

# 예약 취소 버튼 생성
cancel_button = Button(window, text="취소", command=cancel_shutdown)
cancel_button.grid(row=1, column=1)

# GUI 실행
window.mainloop()