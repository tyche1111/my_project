import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('http://www.yes24.com/24/category/bestseller?CategoryNumber=001001025010003&sumgb=06', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
books = soup.select('#category_layout > tbody > tr')

# movies (tr들) 의 반복문을 돌리기
for best20 in books:
    # movie 안에 a 가 있으면,
    # category_layout > tbody > tr:nth-child(1) > td.goodsTxtInfo > p:nth-child(1) > a:nth-child(1)
    a_tag = best20.select_one('tr > td.goodsTxtInfo > p > a')

    print(a_tag)


    # if a_tag is not None:
    #     # goods1
    #     rank = best20.select_one('td:nth-child(1) > img')['alt']  # img 태그의 alt 속성값을 가져오기
    #     title = a_tag.text  # a 태그 사이의 텍스트를 가져오기
    #     star = best20.select_one('td.point').text  # td 태그 사이의 텍스트를 가져오기
    #     print(rank, title, star)
