

class Conta:
    '''
    (self) é a referência que sabe encontrar o objeto que está sendo construido. sendo assim, o endereço da
    memoria que o objeto esta sendo construido

    self. -> para acessar o objeto no endereço
    '''

    def __init__(self, numero, titular, saldo, limite):  # Função construtora
        print('Construindo objeto ...{}'.format(self))
        # Atributos
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    '''
    -> Métodos : Oque o objeto sabe fazer
    -> Atributos: Oque o objeto tem
    '''
    # Métodos
    def extrato(self): # método
        print(f'O saldo de {self.__saldo} do titular {self.__titular}')

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar): # Para avisar que esse método só deve ser utilizado dentro da classe
        valor_desponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_desponivel

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print(f"O valor {valor} passou o limite")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self): # O get sempre tem um retorno
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite): # Um set nunca retorna nada, mas sim muda algo
        self.__limite = limite

    ''' Método da classe -> Métodos estáticos '''
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}

