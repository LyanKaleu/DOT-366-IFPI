def eh_par(num):
    if num % 2 == 0:
        return True
    else:
        return False


def main():
    while True:
        try:
            num = int(input("Digite um número inteiro: "))
            if eh_par(num):
                print("O número é par")
            else:
                print("O número é ímpar")
            break
        except ValueError:
            continue


if __name__ == '__main__':
    main()