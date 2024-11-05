def media(numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma / len(numeros)


def main():
    temperaturas = [23.5, 18.6, 30.2, 15.9, 25.1, 29.8]
    print(f'Temperaturas: {temperaturas}')
    print(f'Média das temperaturas: {media(temperaturas):.2f}°C')



if __name__ == '__main__':
    main()
