from random import randint

def gerar_lista_aleatoria(tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(randint(-1000, 1000))
    return lista


def inverter_lista(lista):
    return lista[::-1]


def main():
    tamanho = int(input('Digite o tamanho da lista: '))
    lista = gerar_lista_aleatoria(tamanho)
    lista_invertida = inverter_lista(lista)

    print(f'\n\nLista gerada: {lista}\n\n')
    print(f'Lista invertida: {lista_invertida}\n\n')

    print(f'Lista invertida à anterior: {inverter_lista(lista_invertida)}')


if __name__ == '__main__':
    main()
