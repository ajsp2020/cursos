idades = [39, 30, 27, 18]

print(type(idades))  # Para descobrir o tipo

print(len(idades))  # para definir o tamanho da lista

print(idades[0])  # Para imprimir um elemento da lista

print(idades)  # para imprimir todos os elemento da lista

idades.append(15)  # Para adicionar um elemento no final da lista
print(idades)

for idade in idades:  # Para passar todos os elementos dentro de um lista
    print(idade)

idades.remove(30)  # Para remover um elemento dentro de uma lista
print(idades)

idades.append(15)
print(idades)

idades.remove(15)  # remove a primeira aparicao do elemento
print(idades, "\n \n")

print(28 in idades)  # para descobri se um elemento esta dentro de uma lista

if 15 in idades:  # remove um elemento se este está dentro de uma lista (o in é muito utilizado para filtrar alguma coisa)
    idades.remove(15)

print(idades)

idades.append(19)
print(idades)

idades.insert(0, 20)  # Para adicionar um elemento em uma posição espefífica da lista.
print(idades)

idades = [20, 39, 18]
print(idades)
idades.extend([27, 19])  # para extender os elementos de uma lista
print(idades)

#  para criar uma nova lista com elementos trabalhados
idades_no_ano_que_vem =[]
for idade in idades:
    idades_no_ano_que_vem.append(idade + 1)

print(idades_no_ano_que_vem)

idades_no_ano_que_vem = [(idade + 1) for idade in idades]
print(idades_no_ano_que_vem)

# Para filtrar um elemento

print([idade for idade in idades if idade > 21])

#  Filtragem para casos mais complexos

def proximo_ano(idade):
    return idade + 1

print([proximo_ano(idade) for idade in idades if idade > 21])


print("\n\n")

#  Melhores métodos para se criar uma lista

def faz_processamento_de_visualização(lista = None):
    if lista == None:
        lista = list()
    print(len(lista))
    print(lista)
    lista.append(13)


faz_processamento_de_visualização()
faz_processamento_de_visualização()




