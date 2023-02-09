import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv


#fonction that get the information of a book 
def info_books(url):
    # do a request on the page to get links of the book
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    #extract info books
    ths = soup.find_all('th')
    tds = soup.find_all('td')
    title = soup.find('h1').text
    images = soup.find_all('img')
    product = soup.find("div", {"id": "product_description"})
    print(product.text)
    description = product.find_next("p").text
    
    # create a csv file to print the information we get 
    print("Livre:", title)
    for th, td in zip(ths, tds):
        print(th.text + ": " + td.text.replace("Â",""))
    print("Description:", description)
    for image in images:
        print(urljoin(url, image['src']))
    print("\n")


