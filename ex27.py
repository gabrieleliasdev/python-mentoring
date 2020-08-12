numeros = [1, 2, 3, 4, 5]
frutas = ['maçãs', 'laranja', 'peras', 'damascos']
carros = [1, 'Corsa', 2, 'Celta', 3, 'gol']

# esse é o primeiro tipo de loop para percorrer uma lista
for numero in numeros:
  print(f"Este é o número: {numero}")

# mesma coisa que o código acima
for fruta in frutas:
  print(f"Uma fruta tipo: {fruta}")

# também podemos pecorrer lista mistas
# perceba que temos que usar um {} uma vez que não sabemos o que já nela
for i in carros:
  print(f"Eu achei {i}")

# também podemos construir listas, primeiro começa com uma vazia
elementos = []

# então use a função range para fazer a contagem de 0 à 5
for i in range (0,6):
  print(f"Adicione {i} para a lista.")
  elementos.append(i)

# agora podemos imprimi-la também
for i in elementos:
  print(f"Elemento era {i}")

