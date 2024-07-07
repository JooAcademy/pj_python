### IT 비전공자를 위한 돈버는 파이썬 코딩
### 인터넷에서 정보 자동 가져오기

from selenium import webdriverfrom 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
service = Service(executable_path=ChromeDriverManager().install()) # 크롬 드라이버 설치
options = webdriver.ChromeOpetions()
options.add_argument('--no-sandbox')
driver = webdriver.Chorme(service=service)








