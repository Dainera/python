# Написать программу, которая собирает посты из группы https://vk.com/tokyofashion
# Будьте внимательны к сайту!
# Делайте задержки, не делайте частых запросов!
#
# 1) В программе должен быть ввод, который передается в поисковую строку по постам группы
# 2) Соберите данные постов:
# - Дата поста
# - Текст поста
# - Ссылка на пост(полная)
# - Ссылки на изображения(если они есть; необязательно)
# - Количество лайков, "поделиться" и просмотров поста
# 3) Сохраните собранные данные в MongoDB
# 4) Скролльте страницу, чтобы получить больше постов(хотя бы 2-3 раза)
# 5) (Дополнительно, необязательно) Придумайте как можно скроллить "до конца" до тех пор пока посты не перестанут добавляться
#
# Чем пользоваться?
# Selenium, можно пользоваться lxml, BeautifulSoup


from pprint import pprint
import time
from pymongo import MongoClient, ASCENDING
from pymongo.collection import Collection
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_DB = "data_collection"
MONGO_COLLECTION = "tokyofashion"

PAGE_ROOT_ID = "page_search_posts"
PAGE_ITEMS_PATH = ".//div[contains(@class,'_post post page_block')]"
PAGE_ITEM_CONTENT_PATH = "_post_content"
PAGE_ITEM_CONTENT_PATH_INNER = "post_content"
PAGE_ITEM_INFO_PATH = "post_info"
POST_TEXT_PATH = "wall_post_text"
POST_LINK_SOURCE_PATH = "post_link"
POST_DATE_PATH = "rel_date"
POST_ITEM_LIKES_PATH = ".//div[contains(@class,'_counter_anim_container')]"
POST_ITEM_SHARES_PATH = ".//span[contains(@class, '_like_button_count')]"
POST_ITEM_VIEWS_PATH = "_views"
POST_SEARCH_LINK = ".//a[@class='ui_tab_plain ui_tab_search']"
POST_SEARCH_INPUT = "wall_search"

MORE_POSTS_LINK = "wall_more_link"

DRIVER_PATH = "./chromedriver.exe"


def print_mongo_docs(cursor):
    for doc in cursor:
        pprint(doc)


def insert_data(collection: Collection, data):
    item = collection.find_one({"post_id": data['post_id']})
    if item is not None:
        collection.replace_one({'_id': item['_id']}, data, upsert=False)
    else:
        collection.insert_one(data)


def check_noise_btn_and_close(driver):
    try:
        btn = driver.find_element(by=By.CLASS_NAME, value="UnauthActionBox__close")
        btn.click()
        time.sleep(5)
        print("Noise message hided")
    except NoSuchElementException:
        pass


def parse_posts(posts_collection, posts_items, skip, driver):
    with MongoClient(MONGO_HOST, MONGO_PORT) as client:
        db = client[MONGO_DB]
        collection = db[MONGO_COLLECTION]
        for post_item in posts_items[skip:]:
            time.sleep(3)

            check_noise_btn_and_close(driver)

            post_id_str = post_item.get_property("id")
            print(post_item.get_property("id"))
            post_content = post_item.find_element(by=By.CLASS_NAME, value=PAGE_ITEM_CONTENT_PATH)

            post_content_inner = post_content.find_element(by=By.CLASS_NAME, value=PAGE_ITEM_CONTENT_PATH_INNER)

            post_info = post_content_inner.find_element(by=By.CLASS_NAME, value=PAGE_ITEM_INFO_PATH)

            post_id = int(post_id_str[-5:])
            print(post_id)

            post = {
                "post_id": post_id,
                "text": post_info.find_element(by=By.CLASS_NAME, value=POST_TEXT_PATH).text,
                'views': post_content_inner.find_element(by=By.CLASS_NAME, value=POST_ITEM_VIEWS_PATH).text,
                'date': post_content.find_element(by=By.CLASS_NAME, value=POST_DATE_PATH).text,
                'likes': post_info.find_element(by=By.XPATH, value=POST_ITEM_LIKES_PATH).text,
                'shares': post_info.find_element(by=By.XPATH, value=POST_ITEM_SHARES_PATH).text,
                'link': post_content.find_element(by=By.CLASS_NAME, value=POST_LINK_SOURCE_PATH).text
            }
            skip += 1

            posts_collection.append(post)
            insert_data(collection, post)

    return skip


def press_search(driver, search_by):
    search_btn = driver.find_element(by=By.XPATH, value=POST_SEARCH_LINK)
    search_btn.click()
    time.sleep(5)
    search_input = driver.find_element(by=By.ID, value=POST_SEARCH_INPUT)
    search_input.send_keys(search_by)
    search_input.send_keys(u'\ue007')
    time.sleep(5)


def collect_data(driver, search_by):
    press_search(driver, search_by)
    count = driver.find_element(by=By.ID, value="page_wall_count_own").value_of_css_property("value")

    posts_collection = []

    skip = 0
    while True:
        print("scrapping ...")
        posts_items = driver.find_elements(by=By.XPATH, value=PAGE_ITEMS_PATH)
        if posts_items is None:
            break

        print(len(posts_items))
        skip = parse_posts(posts_collection, posts_items, skip, driver)
        actions = ActionChains(driver)
        try:
            btn = driver.find_element(by=By.ID, value=MORE_POSTS_LINK)
            actions.move_to_element(btn)
            actions.perform()
            time.sleep(3)
            check_noise_btn_and_close(driver)
        except ElementClickInterceptedException:
            print(skip)
            time.sleep(3)
        time.sleep(10)
        print("scrolled ..")
        print(skip)
        if skip == count:
            break

    return posts_collection


def start_working():
    search_by = input("Search by: ")

    url = 'https://vk.com/tokyofashion'

    load_dotenv()
    service = Service(DRIVER_PATH)
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    time.sleep(5)
    result = collect_data(driver, search_by)

    driver.quit()

    print(result)


start_working()
