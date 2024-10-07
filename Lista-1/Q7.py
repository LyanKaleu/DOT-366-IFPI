def fatorial(num):
    if num == 0:
        return 1
    else:
        return num * fatorial(num - 1)


def main():
    n = int(input('Digite um número inteiro: '))
    print(f'O fatorial de {n} é {fatorial(n)}')


if __name__ == '__main__':
    main()
