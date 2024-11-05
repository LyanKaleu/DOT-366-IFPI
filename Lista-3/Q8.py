from random import randint


max_lista = 5


def gerar_lista(tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(randint(1, 100))
    
    return lista


def gerar_lista_soma_elementos(lista1, lista2):
    if len(lista1) != len(lista2):
        raise ValueError("As listas devem ter o mesmo tamanho.")
    
    soma_elementos = []
    for i in range(len(lista1)):
        soma_elementos.append(lista1[i] + lista2[i])
    
    return soma_elementos


def main():
    lista1 = gerar_lista(max_lista)
    lista2 = gerar_lista(max_lista)
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")

    soma_elementos = gerar_lista_soma_elementos(lista1, lista2)
    print("-=" * 20)
    print(f"Soma dos elementos das listas: {soma_elementos}")
    



if __name__ == '__main__':
    main()
