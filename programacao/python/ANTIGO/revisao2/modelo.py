class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title() # Para colocar todas as primeiras letras de um nome como maiuscula
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Likes: {self._likes}'



class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) # Chama o inicilizador da classe mãe
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Durção: {self.duracao} min - Likes: {self._likes}'


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - Likes: {self._likes}'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):  # Método que define alguém como iterável (duck typing)
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self): # Para retornar o tamanho da playlist
        return len(self._programas)