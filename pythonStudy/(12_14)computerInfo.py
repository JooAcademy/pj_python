### ChatGPT 를 활용한 40가지 파이썬 프로그램 만들기
### 컴퓨터의 정보 확인

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

import psutil
import time

def monitor_resources():
    while True:
        # CPU 사용량
        cpu_percent = psutil.cpu_percent(interval=1)

        # 메모리 사용량
        memory = psutil.virtual_memory()
        ram_percent = memory.percent

        # 네트워크 사용량
        network = psutil.net_io_counters()
        sent_bytes = network.bytes_sent
        recv_bytes = network.bytes_recv

        # 출력
        print(f"CPU 사용량: {cpu_percent}%")
        print(f"RAM 사용량: {ram_percent}%")
        print(f"전송된 바이트: {sent_bytes}")
        print(f"수신된 바이트: {recv_bytes}")
        print("-" * 30)

        # 1초 대기
        time.sleep(1)

if __name__ == "__main__":
    monitor_resources()





