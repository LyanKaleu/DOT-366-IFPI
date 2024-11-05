from random import randint


def gerar_lista(tamanho):
    lista = []
    for i in range(tamanho):
        numero = randint(1, 50)
        lista.append(numero)
    
    return lista


def rotacionar_lista(lista, n):
    n = n % len(lista)
    
    for _ in range(n):
        ultimo = lista[-1]
        for i in range(len(lista) - 1, 0, -1):
            lista[i] = lista[i - 1]
        lista[0] = ultimo
    
    return lista


def main():
    lista = gerar_lista(5)
    print(f'Lista original: {lista}')
    vezes = randint(1, 5)
    print(f'Lista rotacionada {vezes} vezes: {rotacionar_lista(lista, vezes)}')



if __name__ == '__main__':
    main()
