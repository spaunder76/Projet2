import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from books import info_books
import csv
import time

def info_category(url):
    # do a request on the page to get the book informations
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    books = soup.find_all('h3')

    # For every books, get the informations
    for book in books:
        book_url = urljoin(url, book.find('a')['href'])
        info_books(book_url)

    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        footer_element = soup.select_one('li.current')
        # Do more with each page.

        # Find the next page to scrape in the pagination.
        next_page_element = soup.select_one('li.next > a')
        if next_page_element:
            next_page_url = next_page_element.get('href')
            url = urljoin(url, next_page_url)
            info_category(url)
        else:
            break
url = 'https://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
info_category(url)