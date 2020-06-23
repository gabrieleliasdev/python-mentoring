#funções
#nomeiam partes do codigo, assim como variaveis nomeiam string e números
#recebem argumentos da mesma maneira que seus scripts recebem argv
#usando 1 e 2, permitem que vocÊ crie seus proprios "miniscripts" ou "pequenos comandos"

#essa aqui é como seus scripts com argv
def print_dois (*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#o, aquele *args é desnecessário, podemos simplesmnte fazer isso
def print_dois_novamente(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#essa recebe apenas um argumento
def print_um(arg1):
    print(f"arg1': {arg1}")

#essa não recebe argumento nenhum
def print_nenhum():
    print("Recebi nada.")

print_dois("Fabio", "Jilvania")
print_dois_novamente("Fabio", "Jilvania")
print_um("Único!")
print_nenhum()

#o que é permitido para nome da função? qualquer nome que não comece com um número
#e tenha letras, números e sublinhados

#o que faz *em *args? fala para o python obter todos os argumentos e coloca-los no argumentos
