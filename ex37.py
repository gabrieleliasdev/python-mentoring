### Animal é-um object (sim, é meio confuso), veja o crédito extra
class Animal(object):
  pass

## ??
class Cachorro(Animal):
  ## ?
  def __init__(self, nome):
    self.nome = nome

## ??
class Gato(Animal):

  def __init__(self, nome):
  ## ??
    self.nome = nome

class Pessoa(object):

  def __init__(self, nome):
  ## ?
    self.nome = nome

  ##
    self.pet = None

class Empregado(Pessoa):

  def __init__(self, nome, salario):
    super(Empregado, self).__init__(nome)
    self.salario = salario

class Peixe(object):
  pass

class Salmao(Peixe):
  pass

class Vermelho(Peixe):
  pass

charlie = Cachorro("Charlie")

princesa = Gato("Princesa")

maria = Pessoa("Maria")

maria.pet = princesa

frank = Empregado("Frank", 120000)

frank.pet = charlie

nemo = Peixe()

zezinho = Salmao()

ticotico = Vermelho()
