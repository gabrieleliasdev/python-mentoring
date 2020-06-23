# crie um mapeamento entre estados e siglas
estados = {
  'Bahia': 'BA',
  'Pernambuco': 'PE',
  'Alagoas': 'AL',
  'São Paulo': 'SP',
  'Rio de Janeiro': 'RJ'
}
# crie um conjunto básico de cidades
cidades = {
  'BA': 'Feira de Santana',
  'BA': 'Salvador',
  'AL': 'Maceio',
  'PE': 'Caruaru',
  'RJ': 'Cabo Frio'
}
# adicione mais alguma cidades
cidades['SP'] = 'São Paulo'
cidades['RS'] = 'Panambi'
cidades['BA'] = 'Miguel Calmon'

#imprima algumas cidades
print('-' * 10)
print("BA tem", cidades['BA'])

#imprima alguns estados
print('-' * 10)
print("A sigla do estado da Bahia:", estados['Bahia'])
print("A silga do estado de Pernambuco:", estados['Pernambuco'])

# imprima todas as sigla dos estados
print('-' * 10)
for estado, abr in list(estados.items()):
  print(f"{estado} é abreviado por {abr}")
# imprima cada cidade no estado
print('-' * 10)
for abr, cidade in list(cidades.items()):
  print(f"{abr} tem a cidade {cidade}")

# agora faça ambos ao mesmo tempo
print('-' * 10)
for estado, abr in list(estados.items()):
  print(f"{estado} estado é abreviado por {abr}")
  print(f"e tem a cidade {cidades[abr]}")

print('-' * 10)

# com segurança obtenha uma sigla de uma estado que não pode estar ali
estado = estados.get('Piaui')

if not estado:
  print("Desculpe, sem Piaui")
#obtenha uma cidade com um valor padrão
cidade = cidades.get('PI', 'Não existe')
print (f"A cidade para o estado 'PI' é: {cidade}")
