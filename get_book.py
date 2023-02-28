import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

#fonction that get the information of a book 

def writeInfos(csvWriter, title, book_category, ths, tds, description, images, url):
    print("title:", title)
    print("category:", book_category)
    csvWriter.writerow(["Title: " + title])
    csvWriter.writerow(["Category: " + book_category])

    for th, td in zip(ths, tds):
        csvWriter.writerow([th.text + ": " + td.text.replace("Â","")])

    csvWriter.writerow(["Description: ", description])

    for image in images:
        csvWriter.writerow([urljoin(url, image['src'])])

def info_books(url, csvWriter = None):
    # do a request on the page to get links of the book
    response = requests.get(url)
    if response.status_code == 200:
        print("Informations en cours de récupération")
    else:
        print("Une erreure est survenue, veuillez ressayer plus tard")
    soup = BeautifulSoup(response.text, 'lxml')
    #extract books informations
    category = soup.find("li", {"class": "active"})
    book_category = category.find_previous('a').text
    ths = soup.find_all('th')
    tds = soup.find_all('td')
    title = soup.find('h1').text
    images = soup.find_all('img')
    product_description = soup.find("div", {"id": "product_description"})

    if product_description:
        description = product_description.find_next("p").text
    else:
        description = 'Pas de description pour ce livre'

    # create a csv file to print the information we get
    if csvWriter:
        writeInfos(csvWriter, title, book_category, ths, tds, description, images, url)
    else:
        with open('books' + title + '.csv', 'w', newline='') as csvfile:
            csvWriterBook = csv.writer(csvfile, delimiter=';')
            writeInfos(csvWriterBook, title, book_category, ths, tds, description, images, url)
            
info_books('http://books.toscrape.com/catalogue/alice-in-wonderland-alices-adventures-in-wonderland-1_5/index.html')
