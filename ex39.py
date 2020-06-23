'''
Alienígenas invadiram a nave espacial e nosso herói precisa percorrer um labirinto
de salas desmoronando para poder escapar em uma cápsula e ir para o planeta abaixo.
O jogo será parecido com Zork, com saídas de texto e modos divertidos de morrer.
Ele terá um mecanismo que executa um mapa cheio de salas ou cenas.
Cada sala imprimirá sua própria descrição quando o jogador entrar e informará ao mecanismo qual executar em seguida no mapa.
'''
# Morte - quando o jogador morre e dever ser algo divertido ;
# corredor central - o ponto de partida que os jogadores precisam
# derrotar o inimigo com uma piada antes de continuar;
# Arsenal de armas lazer - onde o herói consegue uma bomba de nêutrons
# para explodir a nave antes de entrar na capsula.
# Tem um teclado numero que o herói precisa adivinhar os números
# cápsula - onde o herói escapa, mas só depois de adivinhar qual é a capsula certa
"""jogador , nave, labirinto, Sala, Cena, Inimigo, capsula, planeta, Mapa, mecanismo, morte,"""
""" Corredor central,, Arsenal de armas laser, ponte"""
# o que é semelhante?
# o que é apenas outra palavra para outra coisa?
# Mapa, Mecanismo, Cena(Morte - corredor central, arma a lazer, a ponte, lugar escape)
# Descobrir quais as ações são necessárias em cada item
"""* mapa(- proxima_cena, - abertura_cena)
* mecanismo (- jogar)
* cena (- entrar )
* morte
* corredor central
* arma e lazer
* ponte
* lugar de escape"""

from sys import exit
from random import randint
from textwrap import dedent


class Cena(object):

  def entrar(self):
    print("Essa cena ainda não está configurada.")
    print("Crie uma subclasse dela e implemente entrar().")
    exit(1)

class Mecanismo(object):

  def __init__(self, cena_mapa):
    self.cena_mapa = cena_mapa

  def jogar(self):
    cena_atual = self.cena_mapa.abertura_cena()
    cena_final = self.cena_mapa.proxima_cena('terminado')

    while cena_atual != cena_final:
      proxima_cena_nome = cena_atual.entrar()
      cena_atual = self.cena_mapa.proxima_cena(proxima_cena_nome)

    #certifique-se de imprimir a última cena.
    print("passei aqui")
    cena_atual.entrar()

class Morte(Cena):

  brincadeiras = [
    "Você não conseguiu. Você não é muito bom nisso",
    "Seus amigos devem estar orgulhosos de vocês",
    "Vixe!!!",
    "O gatinho do vizinho é melhor que você"
  ]

  def entrar(self):
    print(Morte.brincadeiras[randint(0,len(self.brincadeiras)-1)])
    exit(1)

class CorredorCentral(Cena):

  def entrar(self):
    print(dedent("""
                Os inimigos invadiram sua nave e destruiram sua tripulação.
                Você é o último sobrevivente e sua útlima missão é pegar uma bomba de neutron na sala de armas,
                e colocar na ponta, e explodir a nave depois de escapar da nave.

                Você está indo pelo corredor central e um inimigo salta em sua frente, ele está bloqueando a
                sua saída e colocou uma arma apontada para você.
                """))

    action = input("> ")

    if action == "atirar!":
      print(dedent("""Rapidamente você pega sua arma e atira no inimigo, mas ele consegue te atacar"""))
      return 'morte'

    elif action == "desviar!":
      print(dedent("""Como um excelente lutador de boxe você consegue se esquivar, mas ele consegue te atacar."""))
      return 'morte'

    elif action == "contar uma piada!":
      print(dedent("""Você é muito bom de piada, o inimigo entra em uma crise de risada"""))
      return 'deposito_armas'

    else:
      print("Não é uma opção válida")
      return 'corredor_central'

class ArmaLaser(Cena):

  def entrar(self):
    print(dedent("""
                Você entra no depósito de armar e procura o container com a arma de neutron.
                Para abrir o container você deve digitar o código, se você errar por 10 vezes as portas
                se fecham para sempre. O código tem 03 digitos.
                """))

    codigo = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
    print(codigo)
    tentativa = input("[keypad]> ")
    tentativas = 0

    while tentativa != codigo and tentativas < 10:
      print("BZZZZZZ")
      tentativas += 1
      tentativa = input("[keypad]> ")

    if tentativa == codigo:
      print(dedent("""
                  O container abre. Você pega a arma de neutron e corre rápido para ponte onde você
                  deve colocar no lugar correto.
                  """))
      return 'a_ponte'

    else:
      print(dedent("""
                  Você escuta pela útlima vez o click do container e seu inimigo consegue destruir
                  toda a nave
                  """))
      return 'morte'

class Ponte(Cena):

  def entrar(self):
    print(dedent("""
                Você chegará até a ponde com sua arma, mas ainda encontra 5 inimigos que tentam controlar
                a nave.
                """))
    action = input("> ")

    if action == "lancar a bomba":
      print(dedent("""
                  Em pânico você consegue  lançar a bomba nos inimifos e morre todo mundo.
                  """))
      return 'morte'

    elif action == "lentamente coloque a bomba":
      print(dedent("""
                  Você consegue colocar a bomba
                  """))

      return 'escape'

    else:
      print("Não é uma opção válida")
      return 'a_ponte'

class Escape(Cena):

  def entrar(self):
    print(dedent("""
                Você corre desesperadamente em busca do local para fugir. Você precisará escolher uma.
                Algumas delas podem danificar, então você não tem tempo para fugir. Existem 5 locais, qual você escolherá?
                """))

    bom_local = randint(1,5)
    print(bom_local)
    tentativa = input("[pod #]> ")

    if int(tentativa) != bom_local:
      print(dedent(f"""
                  Você pula para o local {tentativa} e aperta o botão eject. A capsula não funciona e você
                  fica preso na nave. A bomba explode e todos morrem.
                  """))
      return 'morte'

    else:
      print(dedent(f"""
                  Você pula dentro do local {tentativa} e aperta o botão eject. A capsula é liberada da nave
                  Você consegue ver as bombas explodindo na nave. Você consegue sair são e salvo.
                  Você venceu!!!
                  """))
      return 'final'

class Final(Cena):

  def entrar(self):
    print("Você venceu! Bom trabalho.")
    return exit()

class Mapa(object):

  cenas = {
    'final': Final(),
    'morte': Morte(),
    'escape': Escape(),
    'a_ponte': Ponte(),
    'deposito_armas': ArmaLaser(),
    'corredor_central': CorredorCentral()
  }

  def __init__(self, cena_inicio):
    self.cena_inicio = cena_inicio

  def proxima_cena(self, nome_cena):
    val = Mapa.cenas.get(nome_cena)
    return val

  def abertura_cena(self):
    return self.proxima_cena(self.cena_inicio)

a_mapa = Mapa('corredor_central')
a_game = Mecanismo(a_mapa)
a_game.jogar()
