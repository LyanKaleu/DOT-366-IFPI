from random import randint


max_lista = 5


def gerar_lista(tamanho):
    lista = []
    for _ in range(tamanho):
        lista.append(randint(1, 100))

    return lista


def elevar_ao_quadrado(numero):
    return numero ** 2


def main():
    numeros = gerar_lista(max_lista)
    print(f"Lista gerada: {numeros}")
    
    numeros_ao_quadrado = []
    for numero in numeros:
        numeros_ao_quadrado.append(elevar_ao_quadrado(numero))

    print(f"Números ao quadrado: {numeros_ao_quadrado}")




if __name__ == "__main__":
    main()
