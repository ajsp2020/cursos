import re
email1 = "Meu numero é 1234-1234"
email2 = "Fale comigo em 1234-1234 esse é meu telefone"
email3 = "99234-1234 é o meu celular"
email4 = "Meu numero 9955-2255 ou manda para esse 9326-6655"
email5 = "Meu numero 99552255 ou manda para esse 93266655"

padrao = "[0-9]{4,5}[-][0-9]{4}"

retorno = re.search(padrao, email3)  # Para encontrar o primeiro valor padrao dentro do texto
print(retorno.group())

retorno = re.findall(padrao, email4)  # Para encontrar todos os valores padao dentro do texto
print(retorno)  # Retorna uma lista na ordem que o encontrou

padrao = "[0-9]{4,5}[-]*[0-9]{4}"
retorno = re.findall(padrao, email5)  # Para encontrar todos os valores padao dentro do texto
print(retorno)  # Retorna uma lista na ordem que o encontrou