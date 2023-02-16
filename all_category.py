import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from category import info_category
import csv

def all_category():
    # URL of the Homepage
    home_url = 'http://books.toscrape.com/index.html'

    # Do a request on the homepage to get the links of the category
    response = requests.get(home_url)
    soup = BeautifulSoup(response.text, 'lxml')
    categories = soup.find("div", {"class": "side_categories"})
    print('categories', categories)

    # BODY <---- soup
    # -----| DIV class="side_categories" <---- categories ######
    # ------------| a href="categoryX.html" <----book_categories
    # ------------| span titre
    # ------------| a href="categoryY.html" <----book_categories
    # ------------| a href="categoryZ.html" <----book_categories

    book_categories = categories.find_all('a')
    print('book_categories', book_categories)


    # for each category, get info of the books
    for category in book_categories:
        category_url = urljoin(home_url, category.find('a')['href'])
        category_name = category.find('a')['text']
        print('Category name: ', category_name)
        info_category(category_url, category_name)
        
all_category()