# Необходимо собрать информацию о вакансиях на вводимую должность (используем input) с сайтов Superjob(необязательно)
# и HH(обязательно). Приложение должно анализировать несколько страниц сайта (также вводим через input).
# Получившийся список должен содержать в себе минимум:
# 1) Наименование вакансии.
# 2) Предлагаемую зарплату (отдельно минимальную и максимальную; дополнительно - собрать валюту; можно использовать regexp или if'ы).
# 3) Ссылку на саму вакансию.
# 4) Сайт, откуда собрана вакансия.
# По желанию можно добавить ещё параметры вакансии (например, работодателя и расположение). Структура должна быть
# одинаковая для вакансий с обоих сайтов. Сохраните результат в json-файл
import json

from bs4 import BeautifulSoup
import requests
import time
import re


def search(link, hdr, pos, count):

    html = requests.get(f'{link}/search/vacancy?text={pos}', headers=hdr)
    text = BeautifulSoup(html.text, 'lxml')

    vacancies = []

    for page in range(count):
        main_content = text.find('div', {'id': 'a11y-main-content'})
        tags = main_content.findChildren(recursive=False)

        for tag in tags:
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
                    salaries=salary.getText().split('–')
                    salaries[0] = re.sub(r'[^0-9]', '', salaries[0])
                    salary_min=int(salaries[0])

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

        paging = text.find('a', {'class': 'bloko-button HH-Pager-Controls-Next HH-Pager-Control'})

        if paging is not None:
            time.sleep(42)
            next_btn_link = paging['href']
            html = requests.get(f'{link}{next_btn_link}', headers=hdr)
            text = BeautifulSoup(html.text, 'lxml')
        else:
            break

    return vacancies


headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
position = input("Enter position: ")
pages = int(input("Enter pages count: "))
url = 'https://tula.hh.ru'

result = search(url, headers, position, pages)

print(result)

with open('vacancies.json', 'w') as f:
    json.dump(result, f)


