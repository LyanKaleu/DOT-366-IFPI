def confirmar_resposta():
    while True:
        caractere = input('Deseja continuar? (S/N): ').upper()
        if caractere == 'S' or caractere == 'N':
            return caractere
        else:
            print("Caractere inválido. Digite novamente.")


def calcular_cubo(num):
    return num ** 3


def main():
    while True:
        try:
            numero = float(input('Digite um número: '))
            print(f"O cubo de {numero} é {calcular_cubo(numero)}")
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        if confirmar_resposta() == 'N':
            print("Programa encerrado.")
            break


if __name__ == '__main__':
    main()
