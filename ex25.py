pessoas = 30
carros = 40
caminhoes = 15

if carros > pessoas:
  print('Nós devemos pegar os carros.')
elif carros < pessoas:
  print('Não devemos pegar os carros.')
else:
  print('Não temos que decidir.')

if caminhoes > carros:
  print('Existe muitos caminhões.')
elif caminhoes < carros:
  print('Talvez possamos pegar os caminhões.')
else:
  print('Ainda não podemos decidir.')

if pessoas > caminhoes:
  print('Tudo certo, vamos lá pegar os caminhões.')
else:
  print('Ok, vamos ficar em casa.')

# Se (if) carros > pessoas... se não, então isso (elif), se nenhuma das condições forem atendidas, então (else).
