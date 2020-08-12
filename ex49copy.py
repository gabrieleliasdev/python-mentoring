from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
  global pages
  html = urlopen('https://www.youtube.com/c/VideiraTV/videos{}'.format(pageUrl))
  bs = BeautifulSoup(html, 'html.parser')

  try:
    print(bs.h1.get_text())
    print(bs.find(id='video-title-text').find_all('p')[0])
    print(bs.find(id='ca-edit').find('h3').find('a').attrs['href'])

  except AttributeError:
    print('This page is missing something! Continuig.')

  for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
    if 'href'  in link.attrs:
      if link.attrs['href'] not in pages:
      # encontramos uma página nova
        newPage = link.attrs['href']
        print('-' * 20)
        print(newPage)
        pages.add(newPage)
        getLinks(newPage)

getLinks('')