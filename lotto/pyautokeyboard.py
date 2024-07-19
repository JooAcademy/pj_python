import pyautogui
import time
import webbrowser

# 웹 페이지 열기
webbrowser.open("https://www.g2b.go.kr/pt/menu/selectSubFrame.do?framesrc=/pt/menu/frameGonggong.do?upmu=3&url=https://www.g2b.go.kr:8074/es/srequest/listSvcReqDbrain.do&menuId=001044")

# 웹 페이지가 완전히 로드될 때까지 대기
time.sleep(5)  # 필요에 따라 대기 시간을 조정하세요

# 특정 위치로 이동하여 마우스 클릭
pyautogui.moveTo(500, 500)
pyautogui.click()

# 우클릭
pyautogui.click(button='right')

# 키보드 입력 ('t' 키 누름)
time.sleep(1)  # 우클릭 후 잠시 대기
pyautogui.press('t')
