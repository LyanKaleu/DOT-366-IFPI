def peso_ideal(altura, sexo):
    if sexo == 1:
        peso = (62.1 * altura) - 44.7
    elif sexo == 2:
        peso = (72.7 * altura) - 58
    else:
        return 'Não foi possível calcular o peso ideal. Motivo: Sexo inválido.'

    return f'Peso ideal: {peso:.2f}kg'


def main():
    while True:
        try:
            s = int(input('Digite o seu sexo (1 para feminino, 2 para masculino): '))
            if s != 1 and s != 2:
                print("Sexo inválido.")
                continue

            while True:
                h = float(input('Digite a sua altura em metros: '))
                if 0 < h <= 3:
                    break
                else:
                    print('O valor da altura deve estar entre 0 e 3!')

            print(peso_ideal(h, s))
            break
        except ValueError:
            print('Altura inválida ou sexo inválido.')


if __name__ == '__main__':
    main()
