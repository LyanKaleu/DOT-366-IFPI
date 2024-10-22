def Max(a, b, c, d):
    if a > b and a > c and a > d:
        return a
    elif b > a and b > c and b > d:
        return b
    elif c > a and c > b and c > d:
        return c
    else:
        return d


def main():
    maiores = []

    for i in range(4):
        print(f"Série {i + 1}")

        while True:
            try:
                a1 = int(input("Digite o 1º número: "))
                a2 = int(input("Digite o 2º número: "))
                a3 = int(input("Digite o 3º número: "))
                a4 = int(input("Digite o 4º número: "))
                break
            except ValueError:
                print("Por favor, digite um número válido.")
                continue

        maior = Max(a1, a2, a3, a4)
        maiores.append(maior)

        print(f"O maior número da série é {maior}")
        print("-" * 30)
    
    print(f"O maior número de todas as 4 séries é {Max(maiores[0], maiores[1], maiores[2], maiores[3])}")


if __name__ == '__main__':
    main()
