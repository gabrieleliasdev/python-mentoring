print("""Você pode entrar em duas salas escuras. Você irá pela sala 1 ou pela sala 2?""")

porta = input('>>> ')

if porta == '1':
  print('Existe um urso gigante comendo uma torta.')
  print('O que você faz?')
  print('1. Pegue a torta.')
  print('2. Grite com o urso.')
  urso = input('>>> ')

  if urso == '1':
    print("O urso come seu rosto. Bom trabalho!")
  elif urso =='2':
    print("O urso come suas peras. Bom trabalho!")
  else:
    print(f"Bem, escolher {urso} provavelmente é melhor.")

elif porta == "2":
  print("Você está ohando para uma confeitaria.")
  print("1. Pegue a torta.")
  print("2. Pegue os biscoits.")
  print("3. Pegue os chocolates")

  fome = input(">>> ")

  if fome == "1" or fome == "2":
    print("Você vai engordar um pouquinho.")
  else:
    print("Vai ganhar uns quilos a mais.")

else:
    print("Não irá acontecer nada.")
