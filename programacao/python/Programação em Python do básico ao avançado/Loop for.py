"""
Loop for

loop -> Estrutura de repetição
For => Uma dessas estruturas

C ou Java
for(int i = 0; i < limitador; i++) {
    //execução do loop
}

# Python

for item in interavel:
    //execição do loop


Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis


nome = "Geek University"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

#Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterandd sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 2 (Itenrando sobre um range)
for numero in range(1, 10):
    print(numero)

"""

"""
Enumerate:

((0, 'G), (1, 'e'), (2, 'e'), ....)

for indice, letra in enumerate(nome):
    print(indice)

for indice, letra in enumerate(nome):
    print(letra)
    
# Quando não precisamos de um valorm podemos descartá-lo utilizando um underline(_)
for indice, _ in enumerate(nome):
    print(indice)
    
for valor in enumerate(nome):
    print(valor)


"""
nome = "Geek University"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

"""
# Mais exemplos de for:

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd + 1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma += num
print(f'A soma é {soma}')

# Imprimindo sem pular a linha
for letra in nome:
    print(letra, end='')

"""
# Trabalhando com emojis
# Original: U+1F60D
# Modificado: U0001F60D


for _ in range(3):
    for num in range(1, 11, 2):
        print('\U0001F60D' * num)