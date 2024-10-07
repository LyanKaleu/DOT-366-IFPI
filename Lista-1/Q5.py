def peso_ideal(altura, sexo):
    if sexo == 1:
        peso = (62.1 * altura) - 44.7
    elif sexo == 2:
        peso = (72.7 * altura) - 58
    else:
        return 'Não foi possível calcular o peso ideal. Motivo: Sexo inválido.'

    return f'Peso ideal: {peso:.2f}kg'


def main():
    h = float(input('Digite a sua altura em metros: '))
    s = int(input('Digite o seu sexo (1 para feminino, 2 para masculino): '))
    print(peso_ideal(h, s))


if __name__ == '__main__':
    main()
