# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)
# pip install -r requirements.txt

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"

url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
print(soup.title.text + '\n')

#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")
table_rows = soup.findAll('tr')

"""
headers = []
for header in table_rows[0]:
    if header.text.strip('\n').strip('\n') != '' and header.text.strip('\n').strip('\n') != '#':
        headers.append(header.text.strip('\n').strip('\n'))
"""

# rate = [index, rate]
highest_death_rate = [None, 0.0] 
highest_test_rate = [None, 0.0]
lowest_death_rate = [None, 100.0]
lowest_test_rate = [None, 100.0]

for index, row in enumerate(table_rows[2:52]):
    td = row.findAll('td')
    state = td[1].text.strip('\n')
    total_cases = int(td[2].text.replace(',', ''))
    total_deaths = int(td[4].text.replace(',', ''))
    total_tested = int(td[10].text.replace(',', ''))
    total_population = int(td[12].text.replace(',', ''))

    death_rate = total_deaths / total_cases
    test_rate = total_tested / total_population

    if death_rate > highest_death_rate[1]:
        highest_death_rate = [index + 2, death_rate]
    
    if test_rate > highest_test_rate[1]:
        highest_test_rate = [index + 2, test_rate]
    
    if death_rate < lowest_death_rate[1]:
        lowest_death_rate = [index + 2, death_rate]

    if test_rate < lowest_test_rate[1]:
        lowest_test_rate = [index + 2, test_rate]

backslash = '\n'

print(f"""The state with the highest death rate of {highest_death_rate[1]:.2%} is {table_rows[highest_death_rate[0]].findAll('td')[1].text.strip(backslash)}""")
print(f"""The state with the highest test rate of {highest_test_rate[1]:.2%} is {table_rows[highest_test_rate[0]].findAll('td')[1].text.strip(backslash)}""")
print(f"""The state with the lowest death rate of {lowest_death_rate[1]:.2%} is {table_rows[lowest_death_rate[0]].findAll('td')[1].text.strip(backslash)}""")
print(f"""The state with the lowest test rate of {lowest_test_rate[1]:.2%} is {table_rows[lowest_test_rate[0]].findAll('td')[1].text.strip(backslash)}""")