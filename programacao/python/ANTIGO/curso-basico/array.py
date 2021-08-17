import array as arr
import numpy as np  # Para um melhor desempenho na parte matemática na ultilização de arrays e matrizes

# Um arrat vai tentar otimzar os valores de uma maneira eficiente.
# é nescessário declarar seu tipo.

# evitamos usar array puro. se precisamos de trabalho numérico, é costume usar o numpy.

array = arr.array('d', [1, 3.5])
print(array)

numpy = np.array([1, 3.5])
print(numpy)

print(numpy + 3)