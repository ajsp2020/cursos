class ExtratorArgumentosUrl:
    def __init__(self, url):
        if self.urlEhValida(url):
            self.url = url.lower()
        else:
            raise LookupError("Url inválida!")

    def __len__(self): #  retorna o tamanho da classe
        return len(self.url)

    def __str__(self): #  retorna uma representação em string da classe
        moeda_origem, moeda_destino = self.extraiArgumentos()
        representacao_string2 = self.extrai_valor() + " " + moeda_origem + " " + moeda_destino
        representacao_string = f"Valor: {self.extrai_valor()}\nMoeda Origem: {moeda_origem}\nMoeda destino: {moeda_destino}\n"

        return representacao_string

    def __eq__(self, other): #  para retornar valores iguais quando comparados
        return self.url == other.url

    @staticmethod
    def urlEhValida(url):  # método estático
        if url and url.startswith("https://www.bytebank.com.br"):
            return True
        else:
            return False

    def extraiArgumentos(self):  # Método de instáncia

        buscaMoedaOrigem = "moedaorigem=".lower()
        buscaMoedaDestino = "moedadestino=".lower()



        indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
        indiceFinalMoedaOrigem = self.url.find("&")

        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

        if moedaOrigem == "moedadestino":
            self.trocaMoedaOrigem()
            indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
            indiceFinalMoedaOrigem = self.url.find("&")
            moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

        indiceInicialMoedaDestino = self.encontraIndiceInicial(buscaMoedaDestino)
        indice_final_moeda_destino = self.url.find("&valor=")
        moedaDestino = self.url[indiceInicialMoedaDestino:indice_final_moeda_destino]

        return moedaOrigem, moedaDestino

    def encontraIndiceInicial(self, moedaBuscada):
        return self.url.find(moedaBuscada) + len(moedaBuscada)     

    def trocaMoedaOrigem(self):
        self.url = self.url.replace("moedadestino", "real", 1)
        print(self.url)

    def extrai_valor(self):
        buscar_valor = "valor="
        indice_inicial_valor = self.encontraIndiceInicial(buscar_valor)
        valor = self.url[indice_inicial_valor:]
        return valor