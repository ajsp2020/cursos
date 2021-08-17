class Quadrado:
    def __init__(self, nome, lado):
        self.nome = nome
        self.lado = lado

    def __str__(self):
        return f"Nome = {self.lado} Lado = {self.nome}"


quadradinho = Quadrado("Meu Quadrado", 2)
print(quadradinho)