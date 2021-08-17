def square_sum(numbers):
    soma = 0
    dados = [dado ** 2 for dado in numbers]
    for dado in dados:
        soma += dado
    print(soma)

if __name__ == '__main__':
    square_sum([1, 2])