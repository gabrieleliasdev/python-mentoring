try:
  from setuptools import setup
except ImportError:
    from distutils.core import setup
config = {
  'descripition': 'Meu projeto',
  'author': 'Meu nome',
  'url': 'Url do projeto',
  'download_url': 'Onde baixar o projeto',
  'author_email': 'Meu email',
  'version': '0.1',
  'install_requires': ['nose'],
  'packages': ['NAME'],
  'scripts': [],
  'name': 'nome do projeto'
  }

setup(**config)
