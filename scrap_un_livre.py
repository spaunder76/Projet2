import requests
from bs4 import BeautifulSoup
import time
import pandas
from urllib.parse import urlparse
from urllib.parse import urljoin

links = []

url = 'http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
ths = soup.find_all('th')
tds = soup.find_all('td')
title = soup.find_all('h1')
images = soup.find_all('img')
description = soup.find_all('p')
print(url)

for th,td in zip(ths,tds) : 
    print(th.text + " " + td.text.replace("Â",""))

for h1 in title:
    print("le titre est : ",h1.text)

product = soup.find("div", {"id": "product_description"})
description = product.find_next("p")
print("Description du livre : ", description.text)

for image in images:
    print(urljoin('http://books.toscrape.com',image['src']))