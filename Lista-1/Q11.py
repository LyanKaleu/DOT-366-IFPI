def contar_divisores(n):
    if n <= 0:
        return "O número deve ser inteiro e positivo"

    lista_divisores = []

    for i in range(1, n + 1):
        if n % i == 0:
            lista_divisores.append(i)

    return len(lista_divisores), lista_divisores


def main():
    num = int(input('Digite um número inteiro e positivo: '))
    quantidade, divisores_lista = contar_divisores(num)

    print(f"O número {num} tem {quantidade} divisores.")
    print(f"Os divisores de {num} são: {divisores_lista}")


if __name__ == '__main__':
    main()
