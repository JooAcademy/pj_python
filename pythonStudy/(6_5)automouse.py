### 파이썬과 40개 작품들 
### 4장 10. 오토마우스를 활용한 웹페이지 자동화

'''pip install pyautogui'''
'''pip install pyperclip'''

import pyautogui
import time

while True:
    print(pyautogui.position())
    time.sleep(0.1)

