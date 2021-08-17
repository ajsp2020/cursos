print("")
print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")
print("")

numero_secreto = 42

chute = int(input("Digite o seu numero: "))

acertou = chute == numero_secreto
maior = chute > numero_secreto

if acertou:
    print("Você acertou")
else:
    if maior:
        print("Você errou! O seu chute foi maior que o número secreto")
    else:
        print("Você errou! O seu chute foi menor que o número secreto")
    print("Você errou")

