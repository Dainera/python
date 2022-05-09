# Написать приложение(используя lxml, нельзя использовать BeautifulSoup), которое
# собирает основные новости с сайтов news.mail.ru, lenta.ru, yandex news Для парсинга
# использовать xpath. Структура данных должна содержать:
# название источника(mail и яндекс не источники, а аггрегаторы, см. страницу новости),
# наименование новости,
# ссылку на новость,
# дата публикации

# Сложить все новости в БД, новости должны обновляться, т.е. используйте update


from pprint import pprint

import requests
import time
import re

from bson import ObjectId
from pymongo import MongoClient, ASCENDING
from pymongo.collection import Collection
from lxml.html import fromstring

MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_DB = "homework_3"
MONGO_COLLECTION = "news"


NEWS_ITEMS_PATH = ".//div[contains(@class,'mg-grid__col')]"
NEWS_ROOT_PATH = ".//div"
NEWS_SECTION_PATH = "//section"
NEWS_SOURCE_PATH = ".//a[@class='mg-card__source-link']/text()"
NEWS_DATE_PATH = ".//span[@class='mg-card-source__time']/text()"
NEWS_TITLE_PATH = ".//a[@class='mg-card__link']/text()"
NEWS_LINK_PATH = ".//a[@class='mg-card__link']/@href"
NEWS_LINK_SOURCE_PATH = ".//a[@class='news-story__subtitle']/@href"


def print_mongo_docs(cursor):
    for doc in cursor:
        pprint(doc)


def insert_data(collection: Collection, data):
    item = collection.find_one({"number": data['number']})
    if not None:
        collection.replace_one({'_id': item['_id']}, data, upsert=False)
    else:
        collection.insert_one(data)


def find_source_link(news_item, hdr):
    link = news_item.xpath(NEWS_LINK_PATH)[0]
    time.sleep(42)
    request = requests.get(link, headers=hdr)
    dom = fromstring(request.text)
    return dom.xpath(NEWS_LINK_SOURCE_PATH)


def parse_news(link, hdr):
    request = requests.get(link, headers=hdr)
    dom = fromstring(request.text)

    pprint(request.text)

    section = dom.xpath(NEWS_SECTION_PATH)[0]

    root_path = section.xpath(NEWS_ROOT_PATH)[0]

    news_items = root_path.xpath(NEWS_ITEMS_PATH)

    news_collection = []

    with MongoClient(MONGO_HOST, MONGO_PORT) as client:
        db = client[MONGO_DB]
        collection = db[MONGO_COLLECTION]

        counter = 0
        for news_item in news_items:
            counter += 1
            news = {
                "number": counter,
                'source': news_item.xpath(NEWS_SOURCE_PATH),
                'date': news_item.xpath(NEWS_DATE_PATH),
                'title': news_item.xpath(NEWS_TITLE_PATH),
                'link': find_source_link(news_item, hdr)
            }
            insert_data(collection, news)
            news_collection.append(news)

    return news_collection


def start_working():
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
    url = 'https://yandex.ru/news/'

    result = parse_news(url, headers)

    pprint(result)


start_working()
