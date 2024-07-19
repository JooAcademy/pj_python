from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Chrome 옵션 설정
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # 브라우저 창을 열지 않고 실행
chrome_options.add_argument("--start-maximized")

# ChromeDriver 서비스 생성
service = Service(ChromeDriverManager().install())

# 웹 드라이버 인스턴스 생성
driver = webdriver.Chrome(service=service, options=chrome_options)

# 네이버 금융 페이지 열기
url = "https://finance.naver.com/sise/sise_market_sum.naver"
driver.get(url)

# 페이지 로딩 대기
time.sleep(5)  # 필요한 경우 명시적 대기로 변경

# 페이지 소스 가져오기
html_content = driver.page_source

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html_content, "html.parser")

# 종목명이 들어있는 테이블을 찾음
table = soup.find("table", {"class": "type_2"})

# 테이블에서 종목명 추출
if table:
    rows = table.find_all("tr")[2:47]  # 1위부터 45위까지를 가져옴
    for row in rows:
        # 종목명이 들어있는 첫 번째 td 태그를 찾음
        cols = row.find_all("td")
        if len(cols) >= 2:  # 최소한 2개의 td 태그가 있어야 함
            rank = cols[0].text.strip()  # 순위
            name = cols[1].text.strip()  # 종목명
            print(f"{rank}: {name}")
else:
    print("테이블을 찾을 수 없습니다.")

# 작업 완료 후 브라우저 닫기
driver.quit()
