from sys import exit

def sala_do_ouro():
  print("Essa sala é completamente cheia de ouro. Quanto você vai querer levar?")

  escolha = input(">>> ")

  if "0" in escolha or "1" in escolha:
    quantidade = int(escolha)
  elif int(escolha) < 50:
    print("Perfeito")
    exit(0)
  elif int(escolha) >= 50:
    print("Você errou feio")
  else:
    morte("Cara, aprenda a digitar um número!")

  if quantidade < 50:
    print("Perfeito, você não é ganacioso.")
    exit(0)
  else:
    morte("Você errou feio!")

def sala_do_urso():
  print("Existe um urso aqui.")
  print("O urso tem um monte de mel.")
  print("O urso gordo está na frente da outra porta.")
  print("Como você irá mover o urso?")
  move_urso = False

  while True:
    escolha = input(">>> ")

    if escolha == "pegar mel":
      morte("O urso olha você e arranca a sua face.")
    elif escolha == "provocar urso" and not move_urso:
      print("O urso foi movido da porta.")
      print("Você pode entrar agora.")
      move_urso: True
    elif escolha == "porta aberta" and not move_urso:
      sala_do_ouro()
    else:
      print("Eu não tenho ideia do que isso significa!")

def sala_do_leao():
  print("Nessa sala você verá um grande leão.")
  print("Cuidado para não ficar com medo.")
  print("Você vai lutar ou fugir?")

  escolha = input(">>> ")

  if "lutar" in escolha:
    iniciar()
  elif "fugir" in escolha:
    morte("Isso é tão terrível.")
  else:
    sala_do_leao

def morte(porque):
  print(porque, "Bom trabalho!")
  exit(0)

def iniciar():
  print("Você está na sala escura.")
  print("Existe uma porta para você no lado direito e esquerdo.")
  print("Qual porta você escolherá?")

  escolha = input(">>> ")

  if escolha == "esquerda":
    sala_do_urso()
  elif escolha == "direita":
    sala_do_leao()
  else:
    morte("Você tropeça pela sala até morrer de fome.")

iniciar()
