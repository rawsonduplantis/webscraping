from urllib.request import urlopen, Request 
from bs4 import BeautifulSoup

url = 'https://registrar.web.baylor.edu/exams-grading/spring-2023-final-exam-schedule'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, "html.parser")
print()
print(soup.title.text)
print()
myclasses = ['MW 2:30 p.m.', 'MW 4:00 p.m.', 'TR 2:00 p.m.']
final_rows = soup.findAll("tr")
for row in final_rows:
    final = row.findAll('td')
    if final: 
        myclass = final[0].text
        if myclass in myclasses:
            print(f"For Class: {myclass} the final is scheduled for {final[1].text} at {final[2].text}") 