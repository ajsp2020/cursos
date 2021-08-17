from ExtratorArgumentosUrl import ExtratorArgumentosUrl
'''
argumento = "https://www.bytebank.com.br/cambio?moedaorigem=real"

subString = argumento[5:11]
print(subString)



argumento = "www.bytebank.com/cambio?moedaorigem=real"

index = argumento.find("=")
substring = argumento[index + 1:]
print(substring)

argumentodois ="moedaorigem=real"
listaargumentos = argumentodois.split("=")
print(listaargumentos)

texto = "Izuku Midoriya"
texto[0:10]
texto2 = texto[:4]
print(texto2)
print(texto)

celular = "(41)96574-1728"
indiceInicialCodigoArea = celular.find("(") +1
indiceFinalCodigoArea   = celular.find(")")

print (celular[indiceInicialCodigoArea:indiceFinalCodigoArea])



url = "https://www.bytebank.com.br/cambio?moedaoRigem=moedadestino&moedadestino=dolar&valor=1500"

argumento = ExtratorArgumentosUrl(url)
print(argumento)

print(ExtratorArgumentosUrl.urlEhValida(url))

argumentoUrl = ExtratorArgumentosUrl(url)

moedaOrigem, moedaDestino = argumentoUrl.extraiArgumentos()
print(moedaDestino, moedaOrigem)
print(len(argumentoUrl))
print((argumentoUrl))


valor = argumentoUrl.extrai_valor()
print(valor)


urlByteBank = "https://bytebank.com"
url1 = "https://buscasites.com/busca?q=https://bytebank.com"
url2 = "https://bitebank.com.br"
url3 = "https://bytebank.com/cambio/teste/teste"

print(url3.find(urlByteBank))

print(url3.startswith(urlByteBank))

'''

url = "https://www.bytebank.com.br/cambio?moedaoRigem=moedadestino&moedadestino=dolar&valor=1500"
url2 = "https://www.bytebank.com.br/cambio?moedaoRigem=moedadestino&moedadestino=dolar&valor=2500"

argumentosUrl = ExtratorArgumentosUrl(url)
argumentosUrl2 = ExtratorArgumentosUrl(url2)

print(id(argumentosUrl))
print(id(argumentosUrl2))
print(argumentosUrl == argumentosUrl2)