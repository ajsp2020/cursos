
class Cliente:

    def __init__(self, nome):
        self.__nome = nome


    @property #Método que dá acesso ao objeto
    def nome(self):
        print("chamando o @property nome()")
        return self.__nome.title()


    @nome.setter
    def nome(self, nome):
        print("chamando o setter nome()")
        self.__nome = nome
