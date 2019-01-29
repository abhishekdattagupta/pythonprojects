from __future__ import print_function
import urllib2
from bs4 import BeautifulSoup
import requests

# with open('PythonNotes.txt', 'r') as f:
#     for line in f:
#         print(line, end=' ')

# Using urllib2
wikipage = 'https://en.wikipedia.org/wiki/Hermione_Granger'
page = urllib2.urlopen(wikipage)
soup = BeautifulSoup(page, 'lxml')

# with urllib2.urlopen('https://en.wikipedia.org/wiki/Hermione_Granger') as page:
#     soup = BeautifulSoup(page, 'lxml')

# match = soup.title.text
# match = soup.div
# article = soup.find('div', class_='mw-content-ltr')
# print(match)

for article in soup.find_all('div', class_='mw-parser-output'):
    tiles = article.h3.text
    print(tiles)
    print()

    # summary = article.p.text
    # print(summary)

    # print()
