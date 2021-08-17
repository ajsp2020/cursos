
class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, other):  # Para definir nossa própria condição de igualdade
        if type(other) != ContaSalario:
            return False

        return self._codigo == other._codigo and self._saldo == other._saldo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

class ContaMultiploSalario(ContaSalario):
    pass

conta1 = ContaSalario(37)
conta2 = ContaSalario(37)

print(conta1 == conta2)

conta1.deposita(10)

print(conta1 == conta2)

print("\n\n")

idades = [15, 87, 32, 65, 56, 32, 49, 37]

print(range(len(idades))) # lazy

for i in range(len(idades)):
    print(i, idades[i])

enumerate(idades) # lazy

print(list(range(len(idades)))) # forcei a geração dos valores
print(list(enumerate(idades)))

for valor in enumerate(idades):
    print(valor)

for indice, idade in enumerate(idades):  # unpacking da nossa tupla
    print(indice, idade)

usuarios = [
    ("Guilherme" , 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
]

for nome, idade, nascimento in usuarios:  # já desempacotando
    print(nome)

for nome, _, _ in usuarios:  # já desempacotando. ignorando o resto
    print(nome)

print(sorted(idades))  # Para ordenar as idades

print(list(reversed(idades)))

print(sorted(idades, reverse=True))  # ordenar de forma reversa

print(idades)
idades.sort()  # ordena no próprio lugar a lista
print(idades)

print("\n\n")

conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

for conta in contas:
    print(conta)

def extrai_saldo(conta):
    return conta._saldo

for conta in sorted(contas, key=extrai_saldo):
    print(conta)

from operator import attrgetter

for conta in sorted(contas, key=attrgetter("_saldo")):
    print(conta)

