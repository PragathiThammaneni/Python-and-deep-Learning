#Web scraping - imported the beautifulsoap library

from bs4 import BeautifulSoup
import urllib.request
import os
# define the variable and put the link
url="https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
source_code = urllib.request.urlopen(url)
plain_text = source_code
#Parse the source code using the Beautiful Soup library and save the parsed code in a variable
soup = BeautifulSoup(plain_text, "html.parser")
# print the title and the tags
print(soup.title.string)
for link in soup.find_all('a'):
    print(link.get('href'))
#detected the table and extracted the td and th elements by iterarting over tr attribute
table = soup.find('table', {'class': "wikitable sortable plainrowheaders"})
for row in table.find_all('tr')[1:]:
    columns = row.find_all('td')
    header = row.find('th')
    for column in columns:
        print("<td's>: %s"%(column.text))
    print("<th's>: %s"%(header.text))