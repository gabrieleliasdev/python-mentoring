from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
    html = urlopen('https://www.bibliaonline.com.br/')
    bs = BeautifulSoup(html.read(), 'html.parser')
    print(bs.h1)
except HTTPError as e:
    print(e)
except URLError as e:
    print('O servidor nao foi encontrado')
else:
    print('Funcionou!')
