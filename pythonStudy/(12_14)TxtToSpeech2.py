### ChatGPT 를 활용한 40가지 파이썬 프로그램 만들기
### 글자를 음성으로 변환2 구글 변환기 사용

'''
pip install pyttsx3
pip install gtts
pip install playsound
'''

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


from gtts import gTTS
import os

# 한글 텍스트 입력
text = "안녕하세요. 저는 CLOVA X입니다."

# 음성 변환 객체 생성
tts = gTTS(text=text, lang='ko')

# 음성 파일 생성
tts.save('output.mp3')

# 음성 파일 재생
os.system('output.mp3')


''' playsound 인스톨 에러로 실행 못해봄
from gtts import gTTS
from playsound import playsound

# 한글 텍스트 입력
text = "안녕하세요. 저는 CLOVA X입니다."

# 음성 변환 객체 생성
tts = gTTS(text=text, lang='ko')

# 음성 파일 생성
tts.save('output.mp3')

# 음성 파일 재생
playsound('output.mp3')
'''