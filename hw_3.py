# 1) Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и реализовать функцию,
# записывающую собранные вакансии в созданную БД(добавление данных в БД по ходу сбора данных).
# 2) Написать функцию, которая будет добавлять в вашу базу данных только новые вакансии с сайта.
# 3) Написать функцию, которая производит поиск и выводит на экран вакансии с заработной платой
# больше введённой суммы. Необязательно - возможность выбрать вакансии без указанных зарплат.

import json
from pprint import pprint

from bs4 import BeautifulSoup
import requests
import time
import re
from pymongo import MongoClient, ASCENDING
from pymongo.collection import Collection

MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_DB = "homework_3"
MONGO_COLLECTION = "vacancies"


def print_mongo_docs(cursor):
    for doc in cursor:
        pprint(doc)


def show_vacancies(salary):
    with MongoClient(MONGO_HOST, MONGO_PORT) as client:
        db = client[MONGO_DB]
        collection = db[MONGO_COLLECTION]
        result = collection.find({"$or": [{"salary_max": {"$gt": salary, "$ne": "Not set"}},
                                 {"salary_min": {"$gt": salary, "$ne": "Not set"}}]
        }).sort([
            ("salary_max", ASCENDING),
            ("salary_min", ASCENDING)
        ])
        print_mongo_docs(result)


def insert_data(collection: Collection, data):
    if collection.count_documents({"uri": data['uri']}) > 0:
        return
    collection.insert_one(data)


def parse_vacancy(tag, vacancies, link, collection):
    vacancy = {}
    item = tag.find('span', {'class': 'g-user-content'})
    if item is not None:
        main_info = item.findChild()
        title = main_info.getText()
        vacancy_link = main_info['href']
        salary = tag.find('span', {'class': 'bloko-header-section-3'})
        if not salary:
            salary_min = 'Not set'
            salary_max = 'Not set'
        else:
            salaries = salary.getText().split('–')
            salaries[0] = re.sub(r'[^0-9]', '', salaries[0])
            salary_min = int(salaries[0])

            if len(salaries) > 1:
                salaries[1] = re.sub(r'[^0-9]', '', salaries[1])
                salary_max = int(salaries[1])
            else:
                salary_max = 'Not set'

        vacancy['vacancy'] = title
        vacancy['salary_min'] = salary_min
        vacancy['salary_max'] = salary_max
        vacancy['uri'] = vacancy_link
        vacancy['site'] = link

        vacancies.append(vacancy)
        insert_data(collection, vacancy)


def collect_vacancies(link, hdr, pos, count):
    html = requests.get(f'{link}/search/vacancy?text={pos}', headers=hdr)
    text = BeautifulSoup(html.text, 'lxml')

    vacancies = []

    with MongoClient(MONGO_HOST, MONGO_PORT) as client:
        db = client[MONGO_DB]
        collection = db[MONGO_COLLECTION]
        for page in range(count):
            main_content = text.find('div', {'id': 'a11y-main-content'})
            tags = main_content.findChildren(recursive=False)

            for tag in tags:
                parse_vacancy(tag, vacancies, link, collection)

            paging = text.find('a', {'class': 'bloko-button HH-Pager-Controls-Next HH-Pager-Control'})

            if paging is None:
                break
            else:
                time.sleep(42)
                next_btn_link = paging['href']
                html = requests.get(f'{link}{next_btn_link}', headers=hdr)
                text = BeautifulSoup(html.text, 'lxml')

    return vacancies


def start_working():
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
    position = input("Enter position: ")
    pages = int(input("Enter pages count: "))
    url = 'https://tula.hh.ru'

    result = collect_vacancies(url, headers, position, pages)

    print(result)


start_working()

salary = float(input("Print vacancy with salary more than: "))

show_vacancies(salary)
