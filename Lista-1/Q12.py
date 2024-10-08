def somatorio(num):
    soma = 0
    for i in range(1, num + 1):
        soma += i

    return soma


def main():
    while True:
        try:
            n = int(input('Digite um número inteiro e positivo: '))
            if n <= 0:
                print("O valor deve ser um número inteiro e positivo.")
                continue
            print(f'O somatório de 1 até {n} é {somatorio(n)}')
            break
        except ValueError:
            print("O valor deve ser um número inteiro e positivo.")
            continue


if __name__ == '__main__':
    main()
