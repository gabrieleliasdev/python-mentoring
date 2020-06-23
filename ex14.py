from utils14 import print_mensagem, tamanho_do_cafe

def bot_cafe():
    print("Bem-vindo a nossa Cafeteria!")
    pedir_cafe = 's'
    cafes = []
# [] : Lista, elas podem guardar vários valores ao mesmo tempo, inclusive valores de diferentes tipos

    while pedir_cafe =='s':
      tamanho = tamanho_do_cafe()
      print(tamanho)
      tipo_cafe = pegar_tipo_do_cafe()
# while: Laços, também chamados de “loops”, servem para repetir a execução de um código

      cafe = '{} {}'.format(tamanho, tipo_cafe)
      print('Ok, então {}'.format(cafe))
      cafes.append(cafe)
# append: Indexação - Adição de elemento em determinada posição da lista

      while True:
        pedir_cafe = input('Você gostaria de solicitar outro café? (s/n)')
        if pedir_cafe == 'n':
            break
        elif pedir_cafe == 's':
            break
        print_mensagem()

    print('Ok, então temos:')
    for cafe in cafes:
        print(f'- {cafe}')
    print('Agradecemos a preferência. \n#UseMáscara "Com a Máscara, eu protejo você e você me protege"')
# for (nome) in (objeto): Cada interação/repetição, cafe guadará um caratere da string "cafes",
# na ordem, e, de acordo com a linha seguinte, esse valor será impresso.
# "",'' : Típico uso da

def pegar_tipo_do_cafe():
    res = input("Qual o tipo do café que você deseja?\n[a] Expresso \n[b] Mocha \n[c] Capuccino\n")
    if res == 'a':
      return 'Expresso'
    elif res == 'b':
      return pedir_mocha()
    elif res == 'c':
      return 'Capuccino'
    else:
      print_mensagem()

def pedir_mocha():
    while True:
        res = input('Gostaria de experimentar nossa Edição Limitada de Mocha com pimenta? \n[a] Com certeza! \n[b] Talvez na próxima vez... \n')
        if res == 'a':
              return 'Mocha com pimenta'
        elif res == 'b':
              return 'Mocha'
        else:
          print_mensagem()

bot_cafe()
