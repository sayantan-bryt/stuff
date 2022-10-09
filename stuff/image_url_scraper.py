import os
import requests
from bs4 import BeautifulSoup

names_file = open('names.txt', 'a')
src_file = open('src.txt', 'a')

names_file.write('{')
src_file.write('{')

def image_src_extractor(max_count):
    
    count = 1;
    tail = 'A'
    base_url = "https://www.all-my-favourite-flower-names.com/list-of-flower-names"
    while count <= max_count:
        if count > 1:
            url = base_url + '-' + tail + '.html'
        else:
            url = base_url + '.html'
        const = 'wikimedia'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for img_src in soup.findAll('img'):
            if img_src.get('width') == str(128):
                src = img_src.get('src')
                names = img_src.get('alt')
                if not 'https:' in src:
                    src = 'https:' + src
                
                src_file.write('"' + str(src) + '",\n')
                names_file.write('"' + str(names) + '",\n')

        # for debugging the base_url
        print(url)
        print(count)
        print(tail)
        count += 1;
        tail = chr(ord(tail) + 1)


image_src_extractor(5)

names_file.write('}')
src_file.write('}')

names_file.close()
src_file.close()
