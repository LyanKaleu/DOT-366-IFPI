def fatorial(num):
    if num == 0:
        return 1
    else:
        return num * fatorial(num - 1)


def somatorio_fracionario(num):
    if num > 0:
        soma = 0
        for i in range(1, num + 1):
            soma += 1 / fatorial(i)

        return soma
    else:
        return 'O número deve ser inteiro e positivo.'


def main():
    while True:
        try:
            num = int(input('Digite um número inteiro e positivo: '))
            print(f'Somatório fracionário de 1/{num} = {somatorio_fracionario(num):.2f}')
            break
        except ValueError:
            print('O número deve ser inteiro e positivo.')
            continue


if __name__ == '__main__':
    main()
