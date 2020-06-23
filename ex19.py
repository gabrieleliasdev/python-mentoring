def queijos_e_biscoitos(quantidade_queijo, caixas_de_biscoitos):
    print(f"Você tem {quantidade_queijo} queijos!")
    print(f"Você tem {caixas_de_biscoitos} caixas de biscoitos")
    print(f"Isso é suficiente para uma festa")
    print(f"Pegue um coberto.\n")

print("Nós podemos simplesmente dar os números para as funções diretamente:")
queijos_e_biscoitos(20,30)

print("Ou, nós podemos usar variáveis do nosso script:")
total_de_queijo = 10
total_de_biscoitos = 50

queijos_e_biscoitos(total_de_queijo, total_de_biscoitos)

print("Nós podemos fazer calcúlo também:")
queijos_e_biscoitos(10 + 20,5 + 6)

print("E podemos combinar os dois, variáveis com matématica:")
queijos_e_biscoitos(total_de_queijo + 100, total_de_biscoitos +100)
