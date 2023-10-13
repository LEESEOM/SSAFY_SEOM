import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def get_google_data(keyword):
    url = f'https://www.google.com/search?q={keyword}'

    # 크롬 브라우저가 열림
    # 이 때, 동적인 내용들이 모두 채워진다!
    driver = webdriver.Chrome()
    driver.get(url)

    # 열린 페이지 소스를 받아옴
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 보기 좋게 출력
    print(soup.prettify())

    # response = requests.get(url)

    # # 우리가 얻고자 하는 HTML 내용이 여기에 담김
    # html_text = response.text

    # # HTML을 파싱이 가능한 정리된 형태로 변한
    # soup = BeautifulSoup(html_text, 'html.parser')

    # # 파일로 저장하기
    # with open('soup.txt', 'w', encoding='utf-8') as file:
    #     file.write(soup.prettify())

get_google_data('파이썬')