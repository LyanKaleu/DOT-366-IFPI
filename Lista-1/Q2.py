from math import pi


def calcular_area(raio):
    return pi * raio ** 2


def calcular_perimetro(raio):
    return pi * 2 * raio


def main():
    r = float(input('Digite o raio da circunferência: '))
    print(f'Área: {calcular_area(r):.2f}')
    print(f'Perímetro: {calcular_perimetro(r):.2f}')


if __name__ == '__main__':
    main()
