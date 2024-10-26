from random import randint


max_lista = 10


def gerar_lista(tamanho):
    lista = []
    for i in range(tamanho):
        numero = randint(1, 1000)
        lista.append(numero)

    return lista


def dividir_elementos(lista):
    for i in range(len(lista)):
        if i % 2 == 0:
            lista[i] /= 2
    
    return lista


def multiplicar_elementos(lista):
    for i in range(len(lista)):
        if i % 2 != 0:
            lista[i] *= 3
    
    return lista


def main():
    X = gerar_lista(max_lista)
    print(f"Lista X: {X}")

    Y = dividir_elementos(X)
    Y = multiplicar_elementos(X)
    print(f"Lista Y: {Y}")



if __name__ == '__main__':
    main()
