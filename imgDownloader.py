'''
school = {'sam': 'sits beside me' , 'dean' : 'talks a lot' , 'jenny' : 'asks a lot of questions'}

for i in school:
    print (school[i])
'''

import random
import urllib.request

def download_wed_img(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_wed_img("https://s-media-cache-ak0.pinimg.com/originals/03/6e/80/036e80f092a342711adbed373c4f9c5d.jpg")
