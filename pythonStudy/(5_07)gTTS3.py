### 파이썬과 40개 작품들 
### 3장 3. 텍스트 파일 읽어와서 -> 음성 변환

from gtts import gTTS
from playsound import playsound
import os
import time

# 경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = "mytext.txt"
with open(file_path, "rt", encoding="UTF8") as f:
    read_file = f.read()

tts = gTTS(text = read_file, lang = "ko")

tts.save("myread.mp3")
time.sleep(1)    
playsound("myread.mp3")



