from pattern import title, end, line
from urllib.request import urlopen
from urllib.error import HTTPError # HTTP é o protocolo de navegação entre os navegadores e API
from urllib.error import URLError
from bs4 import BeautifulSoup # BeutifulSoup é uma forma amigavel de pegar o conteúdo do site
title("Interactive Python Scraping")

try:
    site = str(input("Type the site to check its status [www.site.com.br] » ")).strip().lower()
    html = urlopen(site)
    bs = BeautifulSoup(html.read(), 'html.parser')
    print(bs.a)
except HTTPError as e:
    print(e)
except URLError as e:
    print(f'The » \033[4;1;3;31m{site}\033[m « website is currently not acessible!')
else:
    print(f'The » \033[4;1;3;32m{site}\033[m « website is currently accessible!')

line ()
html = urlopen(site)
bs = BeautifulSoup(html.read(), 'html.parser')
nameList = bs.findAll('h3', {'class': 'style-scopetext'})

for name in nameList:
  print(name.get_text())

line ()

def getTitle(url): # função para pegar o titulo. Precisa fornecer o url
  try:
    html = urlopen(url)
  except HTTPError as e:
    return None

  try:
    bs = BeautifulSoup(html.read(), 'html.parser')
    title = bs.body.h3
  except AttributeError as e:
    return None
  return title

title = getTitle(site)
if title == None:
  print('Title could not be found')
else:
  print(title)


