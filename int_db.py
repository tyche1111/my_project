import requests
import datetime
from bs4 import BeautifulSoup

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('http://www.yes24.com/24/category/bestseller?CategoryNumber=001001025010003&sumgb=06',
                    headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
books = soup.select('#category_layout > tr')

# print(books)
now = datetime.datetime.now()
# # books (tr들) 의 반복문을 돌리기
for best20 in books:

    rank_tag = best20.select_one('tr > td')
    #     # movie 안에 a 가 있으면,
    #     # category_layout > tbody > tr:nth-child(1) > td.goodsTxtInfo > p:nth-child(1) > a:nth-child(1)
    a_tag = best20.select_one('tr > td.goodsTxtInfo > p > a')
    # rankimg = best20.select('tr > td.goods1')

    # print(rank_tag, a_tag)

    if a_tag is not None:
        title = a_tag.text
        rank = rank_tag.text

        nowDate = now.strftime('%Y-%m-%d')

        print(rank, title, nowDate)

        doc = {
            'rank': rank,
            'title': title,
            'nowDate': nowDate,

        }
        db.books.insert_one(doc)
    # if a_tag is not None:
    #     # goods1
    #     rank = best20.select_one('td:nth-child(1) > img')['alt']  # img 태그의 alt 속성값을 가져오기
    #     title = a_tag.text  # a 태그 사이의 텍스트를 가져오기
    #     star = best20.select_one('td.point').text  # td 태그 사이의 텍스트를 가져오기
    #     print(rank, title, star)
