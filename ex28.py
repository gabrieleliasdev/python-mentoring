i = 0
numeros = []

while i < 6:
  print(f"No top de i é {i}")
  numeros.append(i)

  i = i + 1
  print("Números agora:", numeros)
  print(f"Na parte final i is {i}")

  print("Os números:")
  for num in numeros:
    print(num)
