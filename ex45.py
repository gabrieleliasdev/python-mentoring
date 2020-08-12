from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://pt.wikipedia.org/wiki/Ballon_d%27Or')
bs = BeautifulSoup(html.read(), 'html.parser')

for child in bs.find('table', {'class': 'wikitable'}).children:
  print(child)
