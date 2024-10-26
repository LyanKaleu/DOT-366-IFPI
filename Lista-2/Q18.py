from random import randint


max_lista = 10


def gerar_lista(tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(randint(-1000, 1000))

    return lista


def copiar_valores_negativos(lista):
    copia = []
    for num in lista:
        if num < 0:
            copia.append(num)
    
    return copia


def main():
    X = gerar_lista(max_lista)
    print(f'Lista X: {X}')

    R = copiar_valores_negativos(X)
    print(f'Lista R: {R}')


if __name__ == '__main__':
    main()
