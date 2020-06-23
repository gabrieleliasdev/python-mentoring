from sys import argv

script, input_file = argv
# Aguardo receber (02) parametros: script: python3 e input_file: Caminho do Arquivo

def imprime_tudo(f):
    print(f.read())

def rebobinar(f):
    f.seek(0)
# seek (0): vai mover o cursor para o inicio do arquivo.

def imprima_uma_linha(numero_linha, f):
    print(numero_linha, f.readline())
# readline: ler apenas um arquivo no texto;

arquivo_atual = open(input_file)

print("Primeiro vamos imprimir todo o arquivo: \n")

imprime_tudo(arquivo_atual)

print("Agora vamos rebobinar, tipo uma fita cassete")

rebobinar(arquivo_atual)

print("Vamos imprimir três linhas:")
linha_atual = 1
imprima_uma_linha(linha_atual, arquivo_atual)
linha_atual = linha_atual + 1
imprima_uma_linha(linha_atual, arquivo_atual)
linha_atual = linha_atual + 1
imprima_uma_linha(linha_atual, arquivo_atual)
