class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):  # Fazer a representação em forma de string dessa classe
        return "[>> Codigo {} Saldo {} <<]".format(self.codigo, self.saldo)


conta_do_gui = ContaCorrente(15)
print(conta_do_gui)

conta_do_gui.deposita(500)
print(conta_do_gui)

conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1000)
print(conta_da_dani)

contas = [conta_do_gui, conta_da_dani]
print(contas)  # neste caso por padrao nao chama a representacao por string da classe

for conta in contas:  # neste caso a representação por string da conta é chamada
    print(conta)

print("\n\n")

# para conseguir alterar todos os objetos da classe dentro de uma lista

def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

contas = [conta_do_gui, conta_da_dani]
deposita_para_todas(contas)
print(contas[0], contas[1])

#  Agora o primeiro elemento da lista contem o numero da agencia

contas.insert(0,76)
print(contas[0], contas[1], contas[2])

# tupla -> é imutável. não pode adicionar ou remover objetos de dentro (usada quando vamos usar tipos diferentes onde não queremos alterar a posição)
# se a posição indica alguma coisa, provavelmente tem um tamanho fixom provavelmente é uma tupla
# Se a posição não tem tipo definido específicom então é tudo do mesmo tipo, não tem que a posição tal tem que ser tal tipo, provavelmente é uma lista)

guilherme = ('Guilherme', 37, 1981)
daniela = ('Daniela', 31, 1987)

def deposita(conta):  # Variação "funcional" (separando o comportamento dos dados)
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    return (codigo, novo_saldo)

conta_do_gui = (15, 1000)
print(conta_do_gui)

conta_do_gui = deposita(conta_do_gui)
print(conta_do_gui)

print("\n\n")

# Lista de tuplas (não podemos alterar o tamanho da tupla)
# a tupla não pode ser alterada, mas nesse caso, o objeto dentro da tupla pode
# Não costuma usar a tupla nesses cenários

usuarios = [guilherme, daniela]
print(usuarios)

usuarios.append(('Paulo', 39, 1979))
print(usuarios)

conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(500)
conta_da_dani = ContaCorrente(1778)
conta_da_dani.deposita(1000)

contas = (conta_do_gui, conta_da_dani)

for conta in contas:
    print(conta)

contas[0].deposita(300)

for conta in contas:
    print(conta)