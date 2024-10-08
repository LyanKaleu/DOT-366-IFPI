def determinar_poligono(num_lados, medida_lado):
    if num_lados == 3:
        return f'TRIÂNGULO\nPerímetro: {num_lados * medida_lado}'
    elif num_lados == 4:
        return f'QUADRADO\nÁrea: {medida_lado ** 2:.1f}'
    elif num_lados == 5:
        return f'PENTÁGONO'
    else:
        return 'Por favor, informe somente os valores 3, 4 ou 5 para número de lados.'


def main():
    while True:
        try:
            n = int(input('Digite o número de lados do polígono (Obs: considere somente os valores 3, 4 ou 5): '))
            if n not in [3, 4, 5]:
                print('Por favor, informe somente os valores 3, 4 ou 5 para número de lados.')
                continue
            m = float(input('Digite a medida do lado do polígono (Obs: considere somente os valores 3, 4 ou 5): '))
            if m not in [3, 4, 5]:
                print('Por favor, informe somente os valores 3, 4 ou 5 para medida do lado.')
                continue
            print(determinar_poligono(n, m))
            break
        except ValueError:
            print("Por favor, digite um número válido.")
            continue


if __name__ == '__main__':
    main()
