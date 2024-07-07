### ChatGPT 를 활용한 40가지 파이썬 프로그램 만들기
### 컴퓨터의 정보 확인2

### pip install psutil

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

import tkinter as tk
import psutil
import time

# GUI 생성
root = tk.Tk()
root.title("CPU, RAM 사용량 모니터링")

# 라벨 생성
cpu_label = tk.Label(root, text="CPU 사용량:")
ram_label = tk.Label(root, text="RAM 사용량:")

# 라벨 위치 설정
cpu_label.grid(row=0, column=0)
ram_label.grid(row=1, column=0)

# CPU 사용량 표시 라벨 생성
cpu_usage_label = tk.Label(root, text="")
cpu_usage_label.grid(row=0, column=1)

# RAM 사용량 표시 라벨 생성
ram_usage_label = tk.Label(root, text="")
ram_usage_label.grid(row=1, column=1)

# 함수 정의
def update_usage():
    # CPU 사용량 업데이트
    cpu_usage = psutil.cpu_percent()
    cpu_usage_label.config(text="{}%".format(cpu_usage))

    # RAM 사용량 업데이트
    ram_usage = psutil.virtual_memory()
    ram_usage_label.config(text="{}MB / {}MB ({}%)".format(ram_usage.used, ram_usage.total, ram_usage.percent))

    # 1초 대기 후 다시 호출
    time.sleep(1)
    root.after(1000, update_usage)

# 함수 호출
update_usage()

# GUI 실행
root.mainloop()