"""
Ranges
- Precisamos conhecer o loop fot para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar seguências numéricas, não de forma aletória, mas sim de maneira especificada.

Formas gerais:

#Forma 1
range(valor_de_parada)

OBS: valor_de_parada não inclusivo (início padrão 0, e passo de 1 em 1)

#for (int i = 0; i < 11; i++):
for i in range(11):
    print(i)

#Forma 2

range(valor_de_inicio, valor_de_parada)

#for (int i = 1; i < 11; i++):
for i in range(1, 11):
    print(i)

#forma 3
range(valor_de_inicio, valor_de_parada, passo)

#for (int i = 1; i < 11; i += 2):
for i in range(1, 11, 2):
    print(i)

#Forma 4 (Inversa)

range(valor_inicio, valor_de_parada, passo)

"""
#for (int i = 10; i > 0; i--):
for i in range(10, 0, -1):
    print(i)

lista = list(range(10))
print(lista)
