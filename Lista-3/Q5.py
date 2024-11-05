def remover_maior(lista):
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior = i

    lista.remove(maior)


def main():
    numeros = [3,6,9,12,15,18]
    print(f'Números antes da remoção: {numeros}')
    remover_maior(numeros)
    print(f'Números após a remoção: {numeros}')


if __name__ == '__main__':
    main()
