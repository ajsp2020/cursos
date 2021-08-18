"""
Listas

Listas em Python funciona com vetores/matrizes (arrays) em outras linguagem, com a diferença de serem DINÂMICO
e também de podermos colocar QUALQUER tipo de dados

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5m estes arrau será SEMPRE
    do tipo inteiro e poderá ter SEMPRE no máximo 5 valores

Já em Python:
    - Dinâmico: Não possui tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
    - Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dados;
    - As listas em Python são representadas pod colchetes: []

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44 ,42, 27]

lista2 = ['A', 'n', 't', 'o', 'n', 'i', 'o']

lista3 = []

lista4 = list(range(11))

lista5 = list('Antonio João')

# Checando se valor está na lista:

num = 8
if num in lista4:
    print(f"Encontrei o numero {num}")

else:
    print(f"Não econtrei o numero {num}")

letra = 'o'

if letra in lista5:
    print(f"Encontrei a letra {letra}")

else:
    print(f"Não econtrei a letra {letra}")

# Ordenando uma lista:

lista1.sort()
print(lista1)

lista5.sort()
print(lista5)

# Contando o numero de ocorrencia de um valor:
print(lista1.count(1))
print(lista5.count('o'))

# Adicinar elemento em listas:

# Para adicionar elementos em lista utilizamos a função append

# OBS; Com append, só se consegue adicionar um elemento por vez

print(lista1)
lista1.append(42)
print(lista1)


lista1.append([8, 3, 1]) # Coloca a lista como elemento único
print(lista1)

if [8, 3, 1] in lista1:
    print("Ecncontrei a lista")
else:
    print("Não encontrei a lista")

lista1.extend([123, 44, 67]) # Coloca cada elemento da lista como elemento adicional á lista (não aceita valor único)
print(lista1)

# Podemos inserir o novo elemento na lista informando a posição do índice
# OBS: Isso não substitui o valor inicial. O mesmo será deslocado para a direita
lista1.insert(2, 'Novo Valor')
print(lista1)


# Podemos facilmente juntar duas listas

lista6 = lista1 + lista2
lista1.extend(lista2)
print(lista6)
print(lista1)



# Podemos facilmente reverter uma lista
# Forma1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

#Forma2
print(lista4[::-1])

# Copiar uma lista

lista6 = lista2.copy()
print(lista6)


# Podemos contar quantos elementos existem dentro da lista
print(len(lista1))

# PODEMOS REMOVER FACILMENTE O ÚLTIMO ELEMENTO DE UMA LISTA:
# OBS: O pop não somente remove o último elemento mas também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice:
#OBS: Os elementos a direita deste índice serão deslocados para a esquerda.
#OBS: Se não houver elemento no índice informado, terermos o erro IndexError.
lista5.pop(2)
print(lista5)


# Podemos remover todos os elementos (zerar a lista)

print(lista5)
lista5.clear()
print(lista5)


# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova *=3
print(nova)


# Podemos facilmente converter ums string para uma lista

# Exemplo 1

curso = 'Programação em Python Essencial'
print(curso)
curso = curso.split()
print(curso)

# OBS: Por padrão, o split separa os elementod da lista pelo espaço entre elas.

#  Exemplo 2

curso = 'Programação,em,Python,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string
print(lista6)

# Abaixo estamos falando: Pega a lista 6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

curso = '$'.join(lista6)
print(curso)


# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados
lista7 = [1, 2.34, True, 'geek', 'd', [1, 2, 3], 45115454]
print(lista7)
print(type(lista7))
"""

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44 ,42, 27]

lista2 = ['A', 'n', 't', 'o', 'n', 'i', 'o']

lista3 = []

lista4 = list(range(11))

lista5 = list('Antonio João')

lista6 = ['Programação', 'em', 'Python', 'Essencial']

