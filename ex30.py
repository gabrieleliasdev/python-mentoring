dez_coisas = "Maçãs Laranjas Corvos Telefones Luz Açúcar"

print("Espero não ter mais de 10 coisas na lista. Vamos arrumar isso.")

material = dez_coisas.split(' ')
mais_coisas = ["Dia", "Noite", "Música", "Tênis", "Pipoca", "Banana", "Garota", "Garoto"]

while len(material) != 10:
  # "enquanto a lista não chegar a 10", essa condição ficará rodando (loop/len) até chegar a 10.
  # Quando chegar a 10 o loop encerra e a próxima linha é executada, no caso, linha 15.
  proximo = mais_coisas.pop()
  print("Adicionar", proximo)
  material.append(proximo)
  # append : esta função irá somar o conteúdo das 02 listas
  print(f"Existem {len(material)} itens agora.")

print("Agora vamos lá: ", material)
print("Vamos fazer mais algumas coisas:")

print("O 2ª material da lista é:", material[1])
print("O 1ª material do final da lista é:", material[-1]) #eita! que chique
print("Que tal remover esse último material da lista?", material.pop())
print("Sendo assim, vamos atualizar nossa lista:", ' '.join(material)) # o que? legal!
print("O 4ª e 6ª item é a nossa prioridade:", ' e '.join(material[3:5])) # show de bola
