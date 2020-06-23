from sys import argv

script, nome_do_arquivo = argv

print(f"Nós vamos apagar um arquivo {nome_do_arquivo}")
print("Se vocẽ não quiser, aperte CTRL + C(^C")
print("Se você quiser, aperte ENTER")

input("?")

print("Abrindo o arquivo...")
target = open(nome_do_arquivo, 'w')
# "w": Permitiu a abertura do arquivo em modo "gravação"

print("Esvaziando o arquivo. Adeus!")
target.truncate()
# truncate: Apagou o contéudo do arquivo

print("Agora vou colocar três linhas")
line1 = input("Line 1:")
line2 = input("Line 2:")
line3 = input("Line 3:")
# input: Permitiu interação com usuário pelo terminal

print("Agora vou inserir as três linhas no arquivo")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# write: Escreveu/lançou o comando do input + interação do usuário dentro do arquivo

print("E finalmente, nos fechamos o arquivo.")
target.close()

# Quando passar o parametro "w" estará dizendo:
# Abra o arquivo em modo gravação
# w = gravação, r = ler, a = anexar
