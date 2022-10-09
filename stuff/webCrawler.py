import requests
from bs4 import BeautifulSoup

def webSpider(max_pages):
    page = 1
    while pages < max_pages:
        url = '' + str(page)                        #delete the page number from the url
        sourceCode = requests.get(url)
        plainText = sourceCode.text
        soup = BeautifulSoup(plainText)
        for link in soup.findAll('a', {'class': 'item-name'}):
            href = '' + link.get('href')
            title = link.string
            print(href)
            print(title)

        page +=1

def get_single_item_data(item_url):
    sourceCode = requests.get(item_url)
    plainText = sourceCode.text
    soup = BeautifulSoup(plainText)
    for item_name in soup.findAll('a', {'class': 'item-name'}):
        print(item_name.string)
    for link in soup.findAll('a'):
        href = '' + link.get('href')


webSpider(max_pages)
