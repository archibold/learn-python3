from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import sys

def get_kod_pocztowy(city, street):
    request = Request("http://00-000.pl/szukaj.php?k=&m={0}&u={1}".format(city, street))
    request.add_header('User-Agent', 'Mozilla/5.0')
    with urlopen(request) as response:
        html_doc = response.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        code = soup.findAll('table')
        for co in code:
            tds = co.findAll('td')
            for td in tds:
                ass = td.find('a')
                if ass and sys.argv[1] in str(ass):
                    if ass.find('strong'):
                        return ass.find('strong').getText()

code = get_kod_pocztowy(sys.argv[1], sys.argv[2])
print(code)
