from random import randint


max_lista = 10


def gerar_lista(tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(randint(-1000, 1000))

    return lista


def inverter_lista(lista):
    lista_invertida = []
    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])

    return lista_invertida


def main():
    D = gerar_lista(max_lista)
    print(f"Lista D: {D}")
    
    E = inverter_lista(D)
    print(f"Lista E: {E}") 


if __name__ == "__main__":
    main()
