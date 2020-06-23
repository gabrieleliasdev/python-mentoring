import random
from urllib.request import urlopen
import sys

PALAVRA_URL = "http://learncodethehardway.org/words.txt"
PALAVRAS = []

FRASES = {
  "class %%%(%%%):":
  "Cria uma classe chamada %%% que é um %%%",
  "class %%%(object):\n\t def __init__(self,***)":
  "class %%% tem-um __init__ que recebe self e *** paramentros.",
  "class %%%(object):\n\t def***(self,@@@)":
  "class %%% tem-uma funcao *** que recebe self e @@@ parametros.",
  "*** = %%%()":
  "Set *** para uma instancia de classe %%%",
  "***.*** = '***'":
  "De *** pegue o *** atributo e setar o valor '***'."
}
# quer treinar primeiro as frases ou os nomes?

if len(sys.argv) == 2 and sys.argv[1] == "english":
  PRIMEIRA_FRASE = True
else:
  PRIMEIRA_FRASE = False

# carregue as palavras do website

for palavra in urlopen(PALAVRA_URL).readlines():
  PALAVRAS.append(str(palavra.strip(), encoding= "utf-8"))

def converte(trecho, frase):
  nomes_classes = [w.capitalize() for w in random.sample(PALAVRAS, trecho.count("%%%"))]
  outros_nomes = random.sample(PALAVRAS, trecho.count("***"))
  resultados = []
  nomes_parametros = []

  for i in range(0, trecho.count("@@@")):
    qtd_parametros = random.randint(1, 3)
    nomes_parametros.append(', '.join(random.sample(PALAVRAS, qtd_parametros)))

  for sentenca in trecho, frase:
    resultado = sentenca[:]

    # nomes de classes falsos
    for palavra in nomes_classes:
      resultado = resultado.replace("%%%", palavra, 1)

    # outros nomes falsos
    for palavra in outros_nomes:
      resultado = resultado.replace("***", palavra, 1)

    # lista de parametros falsas
    for palavra in nomes_parametros:
      resultado = resultado.replace("@@@", palavra, 1)

    resultados.append(resultado)

  return resultados

# continue executando ate que seja digitado o CTRL -D (CTRL -C no windows)
try:
  while True:
    trechos = list(FRASES.keys())
    random.shuffle(trechos)

    for trecho in trechos:
      frase = FRASES[trecho]
      pergunta, resposta = converte(trecho, frase)

      if PRIMEIRA_FRASE:
        pergunta, resposta = resposta, pergunta

      print(pergunta)

      input("> ")
      print(f"RESPOSTA: {resposta}\n\n")
except EOFError:
    print("\nBye")
