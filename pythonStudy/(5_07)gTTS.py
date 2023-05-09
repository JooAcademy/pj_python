### 파이썬과 40개 작품들 
### 3장 3. 텍스트 -> 음성 변환

from gtts import gTTS

text = "안녕하세요. 파이썬과 40개의 작품들 입니다. "
tts = gTTS(text = text, lang = "ko")
tts.save(r"pythonStudy\hi.mp3")



