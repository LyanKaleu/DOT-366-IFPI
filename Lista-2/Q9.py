from random import randint

max_lista = 5

def gerar_lista_numeros(tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(randint(1, 100))
    return lista


def inverter_lista(lista):
    lista_inversa = []

    for i in range(len(lista) - 1, -1, -1):
        lista_inversa.append(lista[i])
    
    return lista_inversa


def main():
    print('-=' * 20)
    print('Lista X:')
    lista = gerar_lista_numeros(max_lista)
    print(lista)
    print('-=' * 20)
    print('Lista Y:')
    lista_inversa = inverter_lista(lista)
    print(lista_inversa)
    print('-=' * 20)


if __name__ == '__main__':
    main()
