"""
Saindo de loops com breaks

Funciona na mesma forma que nas liguagens C ou Java

Utilizamos o break para sair de loops de maneira projetada.

"""

#Exemplo 1

for i in range(1, 11):
    if i == 6:
        break
    else:
        print(i)
print('Sai do loop')


#Exemplo 2

while True:
    comando = input("Digite sair para sair: ")
    if comando == 'sair':
        break
