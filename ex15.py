from sys import argv

script, nome_do_arquivo = argv

txt = open(nome_do_arquivo)

print(f"Aqui está o seu arquivo {nome_do_arquivo}:")
print(txt.read())
# Obs.: A função de leitura/read só é possível se houver a de abertura/open anteriormente

print("Digite o nome do arquivo novamente:")
novo_arquivo = input("> ")
# está função permite interação do terminal para o código
# neste caso, estou chamando o arquivo a ser aberto e lido pelo terminal

print('Segue abaixo para leitura o conteúdo do seu arquivo:')
novo_txt = open(novo_arquivo)

print(novo_txt.read())

# sys : Pacote que já vem com o Python , tem a habilidade de lidar com os comandos nos terminais
# argv : Pertence ao pacote sys, é ele que permite passarmos comandos na linha(script)
# close: é responsável por fechar um arquivo;
# read: vai ler o conteúdo do arquivo;
# readline: ler apenas um arquivo no texto;
# Truncate: esvazia o arquivo;
# write("alguma coisa"): responsável por escrever o arquivo;
# seek (0): vai mover o cursor para o inicio do arquivo.
