
usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

''' 
Criando uma nova listas com elementos de outra
Método 1 
'''
assistiram = []
assistiram.extend(usuarios_data_science)
print(assistiram)

''' 
Método 2 
'''
assistiram = usuarios_data_science.copy()
print("usuarios_data_science.copy():", assistiram)

''' Acrescentando elementos de uma segunda lista '''
assistiram.extend(usuarios_machine_learning)
print("assistiram.extend(usuarios_machine_learning):", assistiram)

''' 
 quando eu tenho uma lista de elementos e não quero pegar os elementos de forma repetida, isso é:
 quero pegar no máximo uma vez cada elemento, temos uma definição que costuma ser usado nessa área de coleções, 
 que é o que chamamos realmente de conjunto em inglês, e aí sim conjunto em inglês, uma palavra técnica 
 é o “set”, S-E-T. -> 
 Obs: Para o set a ordem não importa,
      O conjunto não possuí indexação, sendo assim não pode chamar assistiram[3] por exemplo
 '''

print("set(assistiram):", set(assistiram))

''' Apesar do set não possuir uma ordem definida ele é ainda um iterável, sendo assim: '''

for usuario in set(assistiram):
    print("usuario", usuario)

''' Para pegar usuarios que estão no primeiro conjunto ou no segundo -> neste caso seria "equvalente" ao extend'''

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

print("(usuarios_data_science | usuarios_machine_learning):", usuarios_data_science | usuarios_machine_learning)
