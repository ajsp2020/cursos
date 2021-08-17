
from acesso_cep import BuscaEndereco

#cep = 71915500
#object_cep = BuscaEndereco(cep)
#print(object_cep)

# r = requests.get("https://viacep.com.br/ws/01001000/json/")

#bairro , cidade, uf = object_cep.acessa_via_cep()

#print(bairro, cidade, uf)



def main():
    cep = input("Digite o número do cep: ")

    objeto_cep = BuscaEndereco(cep)
    bairro, cidade, uf = objeto_cep.acessa_via_cep()
    print("Bairro: ", bairro)
    print("Cidade: ", cidade)
    print("UF: ", uf)

cep = main()
