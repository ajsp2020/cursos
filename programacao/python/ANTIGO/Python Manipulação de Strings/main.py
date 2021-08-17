url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500"

argumento = "moedadestino=dolar"

index = argumento.find("=")
print(index)
subString= argumento[index + 1:]
print(subString)

lista = argumento.split("=")
print(lista)