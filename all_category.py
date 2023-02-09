import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from category import info_category
import csv

# URL of the Homepage
home_url = 'http://books.toscrape.com/index.html'

# Do a request on the homepage to get the links of the category
response = requests.get(home_url)
soup = BeautifulSoup(response.text, 'lxml')
categories = soup.find_all('h3')

# for each category, get info of the books
for category in categories:
    category_url = urljoin(home_url, category.find('a')['href'])
    info_category(category_url)
    
