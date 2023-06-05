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


start_x = 1000
start_y = 278
end_x = 1820
end_y = 782

pyautogui.screenshot(r'pythonstudy/서울 날씨.png', region=(start_x, start_y, end_x-start_x, end_y-start_y))








