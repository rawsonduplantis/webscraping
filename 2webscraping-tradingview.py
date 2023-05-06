from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://www.webull.com/quote/us/gainers'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
print(soup.title.text + '\n')

stock_data = soup.findAll('div', attrs={'class': 'table-cells'})
