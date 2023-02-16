import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from books import info_books
import csv
import time

def info_category(url, category_name):
    with open('categories/' + category_name + '.csv', 'w', newline='') as csvfile:
        csvWriter = csv.writer(csvfile, delimiter=';')
        while True:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "lxml")
            books = soup.find_all('h3')

            for book in books:
                book_url = urljoin(url, book.find('a')['href'])
                info_books(book_url, csvWriter)

            next_page_element = soup.select_one('li.next > a')

            if next_page_element:  
                next_page_url = next_page_element.get('href')
                url = urljoin(url, next_page_url)
            else:
                break

url = 'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
info_category(url, 'mystery')