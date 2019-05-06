# from __future__ import print_function
# from urllib2 import urlopen
from bs4 import BeautifulSoup
# import requests

# htmlfile = urlopen(url).read()
# with open('homepage.html', encoding="utf8") as homefile:
#    soup = BeautifulSoup(homefile, 'lxml')


with open('newpage.html', encoding="utf8") as homefile:
    soup = BeautifulSoup(homefile, 'lxml')

# print(soup.prettify())
# match = soup.title.text
# match = soup.find('div', class_='container')
# print(match)
tr1 = soup.find_all('tr')
print(tr1)
# tds = tr1.find(
#    'div', attrs={'name': 'CE informed at', 'contenteditable': 'true'})
# print(tds[0].text)

'''
for tr in soup.find_all('tr')[1:]:
    tds = tr.find_all('td')[0].text  # 0, 1, 7, 10
    print(tds)
'''
# breakpoint()
# for tds in soup.find_all('td')[1:]:
#    trem = tds.find_all('div', attrs={'name': 'Remarks', 'contenteditable': 'true'})[1].text
#    print(trem)

tabcontent = soup.find('table', id='outage_tbl')
# print(tabcontent)

# Remarks = soup.td.find('div', attrs={'name': 'Remarks', 'contenteditable': 'true'})
# print(Remarks)


DateTime = tabcontent.td.find('input',
                              attrs={'name': 'firstSPC', 'id': 'datetimepicker'})
# print(DateTime)

OutageNo = tabcontent.td.find('a',
                              attrs={'name': 'Outage_No', 'id': 'Dropdown11'})
# print(OutageNo)

CEInformedAt = tabcontent.td.find(
    'div', attrs={'name': 'CE informed at', 'contenteditable': 'true'})
# print(CEInformedAt)

# with open('PythonNotes.txt', 'r') as f:
#     for line in f:
#         print(line, end=' ')

# Using urllib2
# wikipage = 'https://en.wikipedia.org/wiki/Hermione_Granger'
# page = urllib2.urlopen(wikipage)
# soup = BeautifulSoup(page, 'lxml')

# with urllib2.urlopen
# ('https://en.wikipedia.org/wiki/Hermione_Granger') as page:
#     soup = BeautifulSoup(page, 'lxml')

# match = soup.title.text
# match = soup.div
# article = soup.find('div', class_='mw-content-ltr')
# print(match)

# for article in soup.find_all('div', class_='mw-parser-output'):
#    tiles = article.h3.text
#    print(tiles)
#    print()

# summary = article.p.text
# print(summary)

# print()
