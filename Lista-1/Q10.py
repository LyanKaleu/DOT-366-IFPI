def Max(a, b):
    if a > b:
        return a
    else:
        return b


def main():
    for i in range(4):
        print(f"Série {i + 1}")

        a1 = int(input("Digite o 1º número: "))
        a2 = int(input("Digite o 2º número: "))
        a3 = int(input("Digite o 3º número: "))
        a4 = int(input("Digite o 4º número: "))

        maior = Max(a1, a2)
        maior = Max(maior, a3)
        maior = Max(maior, a4)

        print(f"O maior número da série é {maior}")
        print("-" * 30)


if __name__ == '__main__':
    main()
