import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta
import datetime

# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('http://www.yes24.com/24/category/bestseller?CategoryNumber=001001025010003&sumgb=06',
                    headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# url = soup.find_all('img')
#
# print(url)
#
# for i in url:
#     print(i.get('src'))

# og_image = soup.select_one('meta[property="og:image"]')
# url_image = og_image['content']
#
# print(url_image)

# select를 이용해서, tr들을 불러오기
books = soup.select('#category_layout > tr')

# category_layout > tbody > tr:nth-child(1) > td.image > div > a:nth-child(1) > img

# category_layout > tbody > tr:nth-child(1) > td.image > div > a:nth-child(1) > img

now = datetime.datetime.now()
# # books (tr들) 의 반복문을 돌리기
for best20 in books:

    rank_tag = best20.select_one('tr > td')

    a_tag = best20.select_one('tr > td.goodsTxtInfo > p > a')

    img_url = best20.select_one('td.image > div > a:nth-child(1) > img')

    if a_tag is not None:
        img = img_url['src'].replace('/S', '')

        print(img)

        title = a_tag.text
        rank = rank_tag.text

        nowDate = now.strftime('%Y-%m-%d')

        # print(rank, title, nowDate)

        doc = {

            'rank': rank,
            'title': title,
            'nowDate': nowDate,

        }
        # db.books.insert_one(doc)

# print(a_tag)
# print(rank_tag, a_tag)
