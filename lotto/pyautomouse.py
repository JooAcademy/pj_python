import pyautogui
import time

# 화면 크기 출력
print(pyautogui.size())

# 현재 마우스 위치
x, y = pyautogui.position()
print(x, y)

# 마우스 이동 및 우클릭
pyautogui.moveTo(500, 500, duration=1)  # 커서 이동 위치 (1초 동안 이동)
pyautogui.click(button='right')  # 우클릭
time.sleep(1)  # 1초 대기

# 원래 위치로 마우스 이동
pyautogui.moveTo(x, y, duration=1)  # 1초 동안 원래 위치로 이동
