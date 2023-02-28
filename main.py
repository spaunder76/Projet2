import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from get_category import info_category
import csv
from time import sleep
from tqdm import tqdm

def delete_all(string, values):
    for value in values:
        string = string.replace(value, "")
    return string

def all_category():
    # URL of the Homepage
    home_url = 'http://books.toscrape.com/index.html'

    # Do a request on the homepage to get the links of the category
    response = requests.get(home_url)
    soup = BeautifulSoup(response.text, 'lxml')

    # categories = soup.find("ul", {"class": "nav-list"})
    # book_categories = categories.find_all('a')

    # print(soup)
    categories = soup.find_all("ul")
    menu_categories = categories[1]
    book_categories = menu_categories.find_all('li')
    # Remove first elem
    book_categories.pop(0)

    # for each category, get info of the books
    for book_category in tqdm(book_categories):
        category_url = urljoin(home_url, book_category.find('a')['href'])
        category_name = book_category.find('a').contents[0]
        category_transformed = delete_all(category_name, ['\n', '$', ' '])
        print('Category name:', category_transformed)
        info_category(category_url, category_transformed)

all_category()
