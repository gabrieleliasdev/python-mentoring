from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

# Coleta uma lista de todos URL externos encontrados no site
allExtLinks = set()
allIntLinks = set()

#obtem uma lista de todos os links internos encontrados em uma pagína
def getInternalLinks(bs, includeUrl):
  includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
  internalLinks = []

  # Encontra todos os links que começam com "/"
  for link in bs.find_all('a', href=re.compile('^(/|.*'+includeUrl+')')):
    if link.attrs['href'] is not None:
      if link.attrs['href'] not in internalLinks:
        if (link.attrs['href'].startswith('/')):
          internalLinks.append(includeUrl + link.attrs['href'])
        else:
          internalLinks.append(link.attrs['href'])
  return internalLinks

# Obtem uma lista de todos os link externos encontrados em uma página
def getExternalLinks(bs, excludeUrl):
  externalLinks = []

  # Encontra todos os links que começam com http e que não contenham url atual
  for link in bs.find_all('a', href=re.compile('^(http|wwww)((?!' + excludeUrl + ').)*$')):
    if link.attrs['href'] is not None:
      if link.attrs['href'] not in externalLinks:
        externalLinks.append(link.attrs['href'])
  return externalLinks

def getRandomExternalLink(startingPage):
  html = urlopen(startingPage)
  bs = BeautifulSoup(html, 'html.parser')
  externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)
  if len(externalLinks) == 0:
    print('No external links, looking around the site for one')
    domain = '{}://{}'.format(urlparse(startingPage).scheme, urlparse(startingPage).netloc)
    internalLinks = getInternalLinks(bs, domain)
    return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks) -1)])
  else:
    return externalLinks[random.randint(0, len(externalLinks) -1)]

def followExternalOnly(startingSite):
  externalLink = getRandomExternalLink(startingSite)
  print('Random external link is: {}'.format(externalLink))
  followExternalOnly(externalLink)

def getAllExternalLinks(siteUrl):
  html = urlopen(siteUrl)
  domain = '{}://{}'.format(urlparse(siteUrl).scheme, urlparse(siteUrl).netloc)
  bs = BeautifulSoup(html, 'html.parser')
  internalLinks = getInternalLinks(bs, domain)
  externalLinks = getExternalLinks(bs, domain)

  for link in externalLinks:
    if link not in allExtLinks:
      allExtLinks.add(link)
      print(link)

  for link in internalLinks:
    if link not in allIntLinks:
      allIntLinks.add(link)
      getAllExternalLinks(link)

allIntLinks.add('http://oreilly.com')
getAllExternalLinks('http://oreilly.com')
followExternalOnly('http://oreilly.com')
