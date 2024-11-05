from random import randint


max_lista = 5


def gerar_lista(tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(randint(1, 10))
    
    return lista


def soma_pares_elementos(lista, k):
    pares = []

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == k:
                pares.append((lista[i], lista[j]))

    return pares


def main():
    lista = gerar_lista(max_lista)
    print(f"Lista: {lista}")
    
    while True:
        try:
            k = int(input("Digite o valor de k: "))
            pares = soma_pares_elementos(lista, k)
            if len(pares) == 0:
                print("Nenhum par de elementos da lista soma à k.")
            else:
                print(f"Pares de elementos que somam à {k}:")
                print(pares)
        except ValueError:
            print("O valor de k deve ser um número inteiro.")
            continue


if __name__ == '__main__':
    main()
