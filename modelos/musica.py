class Musica:
    def __init__(self, nome='', artista='', duracao=0):        
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica1 = Musica('Mesmo sem entender', 'Thalles Roberto', 355)

print(vars(musica1))