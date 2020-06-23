# String, Bytes e Codificação de Caractéres
import sys
script, encoding, erro = sys.argv

def main(arquivo_linguagem, encoding, erros):
# main(): A função será executada apenas neste módulo. Evitar transfiguração de linguagem.
    linha = arquivo_linguagem.readline()

    if linha:
        imprima_linha(linha, encoding, erros)
        return main(arquivo_linguagem, encoding, erros)

def imprima_linha(linha, encoding, erros):
    prox_ling = linha.strip()
#strip(): Retira espaços em branco no começo e no fim
    dados_bytes = prox_ling.encode(encoding, erros)
#encode(): Método para especificar a codificação
    dados_string = dados_bytes.decode(encoding, erros)
#decodificação(): Método para especificar o formato de codificação decodificação sequências codificadas
    print(dados_bytes, "<===>", dados_string)

linguagem = open("linguagens.txt", encoding="utf-8")
# Aqui o arquivo a ser aberto já foi especifiado, faltando acrescentar em terminal: utf-8 strict

main(linguagem, encoding, erro)

# encode(): sintaxe do método: str.encode(encoding='UTF-8',errors='strict')
#         : Parâmetros para erros
#         : Este método retorna uma string codificada

# decodificar(): sintaxe do método: str.decode(encoding='UTF-8',errors='strict')
#              : Parâmetros para erros
#              : Este método retorna uma string decodificada
