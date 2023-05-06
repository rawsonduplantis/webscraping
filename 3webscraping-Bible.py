import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

chapters = list(range(1,22))
random_chapter = random.choice(chapters)

if random_chapter < 10:
    random_chapter = '0'+ str(random_chapter)
else:
    random_chapter = str(random_chapter)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
url = 'https://ebible.org/asv/JHN' + '10' + '.htm'

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
print(soup.title.text + '\n')

data = soup.find_all('div', class_='p')
verses = []

""" for paragraph in data:
    #print(paragraph.text + '\n')
    for verse in paragraph:
        if verse.text.isnumeric() == False and verse.text.__contains__('\xa0') == False:
            verses.append(verse.text)
            print(verse.text) """

import keys
from twilio.rest import Client

client = Client(keys.account_sid, keys.auth_token)

TWnumber = ''
myphone = ''