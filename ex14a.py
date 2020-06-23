def tipo_do_cafe():
    res = input("Qual o tipo do café que você deseja?\n[a] Expresso \n[b] Mocha \n[c] Capuccino\n")
    if res == 'a':
      return 'Expresso'
    elif res == 'b':
      return 'Mocha'
    elif res == 'c':
      return 'Capuccino'
    else:
      print_mensagem()
      tipo_do_cafe()

def tamanho_do_cafe():
    res = input("Qual é o tamanho do café que você deseja?\n[a] Pequeno \n[b] Médio \n[c] Grande\n")
    if res == 'a':
      return 'Pequeno'
    elif res == 'b':
      return 'Médio'
    elif res == 'c':
      return 'Grande'
    else:
      print_mensagem()
      tamanho_do_cafe()

def print_mensagem():
    print("Me desculpe. Não compreende o que você disse. Por favor, entre com a letra correta.")
