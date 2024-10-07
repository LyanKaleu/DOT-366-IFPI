def somatorio(num):
    if num <= 0:
        return "O valor deve ser um número inteiro e positivo."

    soma = 0
    for i in range(1, num + 1):
        soma += i

    return soma


def main():
    n = int(input('Digite um número inteiro e positivo: '))
    print(f'O somatório de 1 até {n} é {somatorio(n)}')


if __name__ == '__main__':
    main()
