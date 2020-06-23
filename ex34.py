class Musica(object):
  def __init__(self, letras):
    self.letras = letras

  def cante_uma_musica(self):
    for linha in self.letras:
      print(linha)

parabens = Musica(["Parabéns para você",
"Nessa data querida", "Muitas felicidades",
"Muitos anos de vida"])

louvor = Musica(["Todas as coisas cooperam", "para o bem", "daqueles que o amam"])

parabens.cante_uma_musica()
louvor.cante_uma_musica()
