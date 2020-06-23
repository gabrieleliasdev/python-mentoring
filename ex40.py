class Pai(object):

  def implicito(self):
    print("PAI implicito()")

  def sobrescreve(self):
    print("Pai sobrescreve()")

  def alterada(self):
    print("Pai alterada()")

class Filho(Pai):

  def sobrescreve(self):
    print("Filho sobrescreve()")

  def alterada(self):
    print("Filho, Antes Pai alterada()")
    super(Filho, self).alterada()
    print("Filho, Depois Pai alterada()")

pai = Pai()
filho = Filho()

#pai.implicito()
#filho.implicito()

#pai.sobrescreve()
#filho.sobrescreve()

pai.alterada()
filho.alterada()
