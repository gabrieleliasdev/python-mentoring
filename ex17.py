from sys import argv
from os.path import exists
# os,path: Acessa os arquivos na área do diretório, neste caso do VS Code

script, do_arquivo, para_arquivo = argv
# script = argv : presume-se interação no terminal para rodar o Code

print(f"Copiando do arquivo {do_arquivo} para o arquivo {para_arquivo}")
#trouxe ao print os nomes dos arquivos apresentados pelo usuário ao startar o code

no_arquivo = open(do_arquivo)
no_dado = no_arquivo.read()
#O arquivo a ser copiado será aberto e lido pelo code.

print(f"O tamanho do arquivo é {len(no_dado)} bytes")
#len: Essa função retorna a quantidade de elementos de qualquerlista em Python

print(f"O arquivo existe? {exists(para_arquivo)}")
# exists: Tem a função de verificar se determinado arquivo existe.
print(f"Pronto, aperte Enter para continuar, CTRL + C para abortar")
input()

saida_arquivo = open(para_arquivo, "w")
# O parametro "w" tem a capacidade de criar arquivos, quando chamado em uma função
saida_arquivo.write(no_dado)


print("Ok, tudo bem!")

saida_arquivo.close()
no_arquivo.close()

# Parâmetros: são os nomes dados aos atributos que uma função pode receber
# Argumentos: são os valores que realmente são passados para uma função
