class MinhaClasse(object):

  tangerina = ""
  laranja = ""
  def __init__(self):
    self.tangerina = "Bergamato"
    self.laranja = "Laranja"
  def maca(self, fruta):
    print('Eu sou um classe de maçãs', fruta)

minhaClasse = MinhaClasse()
minhaClasse.maca('uva')
print(minhaClasse.tangerina, minhaClasse.laranja)
