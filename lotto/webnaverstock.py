import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.naver"

# 웹 페이지에 접속
response = requests.get(url)
html_content = response.text

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
