import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib.request
import shutil

home_url = 'http://books.toscrape.com/index.html'

def download_images(url):
    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        images = soup.find_all('img')

        for image in images:
            image_url = (urljoin(url, image['src']))
            filename = image_url.split("/")[-1]

            # Open the url image, set stream to True, this will return the stream content.
            r = requests.get(image_url, stream = True)

            # Check if the image was retrieved successfully
            if r.status_code == 200:
                # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
                r.raw.decode_content = True
                
                # Open a local file with wb ( write binary ) permission.
                with open('images/' + filename,'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                    
                print('Image sucessfully Downloaded: ', filename)
            else:
                print('Image Couldn\'t be retreived')

        next_page_element = soup.select_one('li.next > a')
        if next_page_element:
            next_page_url = next_page_element.get('href')
            url = urljoin(home_url, next_page_url)
            if "catalogue" not in next_page_url:
                url = urljoin("http://books.toscrape.com/catalogue/", next_page_url)
            print('Next page')
        else:
            print('End of pagination')
            break

download_images(home_url)
