def quebrar_palavras(mensagem):
  """Esta função irá dividir palavras para nós."""
  palavras = mensagem.split(' ')
  return palavras

def ordenar_palavras(mensagem):
  """Ordenar as palavras"""
  return sorted(mensagem)

def imprima_primeira_palavra(palavras):
  """Imprime a palavra depois de tirá-la do conjunto"""
  palavra = palavras.pop(0)
  print(palavra)

def imprima_ultima_palavra(palavras):
  """Imprime a ultima palavra depois de tira-la do conjunto"""
  palavra = palavras.pop(-1)
  print(palavra)

def ordenar_mensagem(mensagem):
  """Recebe uma frase completa e retorna as palavras ordenadas."""
  palavras = quebrar_palavras(mensagem)
  return ordenar_palavras(palavras)

def imprima_primeira_e_ultima(mensagem):
  """Imprime a primeira e ultima palavra de uma frase."""
  palavras = quebrar_palavras(mensagem)
  imprima_primeira_palavra(palavras)
  imprima_ultima_palavra(palavras)

def imprima_primeira_e_ultima_ordenada(mensagem):
  """Ordena as palavras e então imprime a primeira e ultima"""
  palavras = ordenar_mensagem(mensagem)
  imprima_primeira_palavra(palavras)
  imprima_ultima_palavra(palavras)

# >>> from ex23 import * >>> sentenca = "mensagem" >>> def à ser executada
# String: sentenca, não tem um atributo pop
# pop(0) pop(-1) = Método, função de Lista, logo ele responde apenas à uma Lista
# by term.- import ex23: Definindo apenas import, terá de acusar ex23. (from) como pré-fixo
# by term.- from ex23 import *: Ao definir from/import, as funções poderão ser executas diretamente
# help(ex23) = Consulta as funções e seus comentário, sabendo assim sobre o que se trata, sem precisar executa-la
# """ = 03 Aspas Duplas é a documentação do código, nela descreve a função do código, visando futura consulta
