from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://pt.wikipedia.org/wiki/Ballon_d%27Or')
bs = BeautifulSoup(html.read(), 'html.parser')
nameList = bs.findAll('span', {'class': 'toctext'})

for name in nameList:
  print(name.get_text())
