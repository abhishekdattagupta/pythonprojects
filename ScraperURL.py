from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://en.wikipedia.org/wiki/Hermione_Granger'
htmlfile = urlopen(url).read()
soup = BeautifulSoup(htmlfile, 'lxml')

# print(soup.prettify())

match = soup.find('div', class_='mw-parser-output')
# print(match)

for article in soup.find_all('div', class_='mw-parser-output'):
    MovieTitle = article.find_all('h3')

print(len(MovieTitle))

for h3 in MovieTitle[0:7]:
    nametitle = h3.find('span', class_='mw-headline')
    print(nametitle.text)

