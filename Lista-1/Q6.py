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
    n = int(input('Digite o número de lados do polígono (Obs: considere somente os valores 3, 4 ou 5): '))
    m = float(input('Digite a medida do lado do polígono (Obs: considere somente os valores 3, 4 ou 5): '))
    print(determinar_poligono(n, m))


if __name__ == '__main__':
    main()
