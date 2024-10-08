def somatorio_fracionario(num):
    if num > 0:
        soma = 0
        for i in range(1, num + 1):
            soma += ((i ** 2) + 1) / (i + 3)

        return soma
    else:
        return 'O número deve ser inteiro e positivo.'


def main():
    while True:
        try:
            num = int(input("Digite um número: "))
            print(f"Somatório fracionário = {somatorio_fracionario(num)}")
            break
        except ValueError:
            print("O número deve ser inteiro e positivo.")


if __name__ == '__main__':
    main()
