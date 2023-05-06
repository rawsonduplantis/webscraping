import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

url = 'https://biblehub.com/asv/john/1.htm'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
print(soup.title.text + '\n')

data = soup.find_all('p', class_='reg')
verses = []

for paragraph in data:
    for verse in paragraph:
        if verse.text.isnumeric() == False:
            verses.append(verse.text.replace(' \r\n', ''))

print(f"Number of verses: {len(verses)}")

print(random.choice(verses))