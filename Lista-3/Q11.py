from random import randint


def gerar_lista(tamanho):
    lista = []
    for _ in range(tamanho):
        lista.append(randint(0, 100))

    return lista


def intercalar_listas(lista1, lista2):
    lista_intercalada = []

    if len(lista1) > len(lista2):
        for i in range(len(lista2)):
            lista_intercalada.append(lista1[i])
            lista_intercalada.append(lista2[i])
        for i in range(len(lista2), len(lista1)):
            lista_intercalada.append(lista1[i])
    else:
        for i in range(len(lista1)):
            lista_intercalada.append(lista1[i])
            lista_intercalada.append(lista2[i])
        for i in range(len(lista1), len(lista2)):
            lista_intercalada.append(lista2[i])

    return lista_intercalada


def main():
    lista1 = gerar_lista(3)
    lista2 = gerar_lista(5)
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print(f"Lista intercalada: {intercalar_listas(lista1, lista2)}")


if __name__ == '__main__':
    main()
