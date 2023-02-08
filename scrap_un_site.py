import requests
from bs4 import BeautifulSoup
import time
import pandas
from urllib.parse import urlparse
from urllib.parse import urljoin
from scrap_un_livre import info_books
from scrap_une_categorie import info_categorie
import csv

# URL de la page d'accueil
home_url = 'http://books.toscrape.com/index.html'

# Effectue une requête sur la page d'accueil pour récupérer les liens vers les catégories
response = requests.get(home_url)
soup = BeautifulSoup(response.text, 'lxml')
categories = soup.find_all('h3')

# Pour chaque catégorie, récupère les informations sur les livres
for category in categories:
    category_url = urljoin(home_url, category.find('a')['href'])
    info_categorie(category_url)
