def fatorial(num):
    if num == 0:
        return 1
    else:
        return num * fatorial(num - 1)


def main():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
            print(f'O fatorial de {n} é {fatorial(n)}')
            break
        except ValueError:
            print("Por favor, digite um número válido.")
            continue


if __name__ == '__main__':
    main()
