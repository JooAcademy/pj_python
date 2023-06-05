### 파이썬과 40개 작품들 
### 4장 10. 오토마우스를 활용한 웹페이지 자동화

'''pip install pyautogui'''
'''pip install pyperclip'''

import pyautogui
import time
import pyperclip

pyautogui.moveTo(1300, 232, 0.2)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("서울 날씨")
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)


