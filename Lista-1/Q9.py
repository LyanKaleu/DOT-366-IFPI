def somar_numeros_intervalo(n1, n2):
    soma = 0
    if n1 < n2:
        for n in range(n1, n2 + 1):
            soma += n
    else:
        for n in range(n2, n1 + 1):
            soma += n

    return soma


def main():
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    print(f'A soma dos números no intervalo [{n1}, {n2}] é {somar_numeros_intervalo(n1, n2)}')


if __name__ == '__main__':
    main()
