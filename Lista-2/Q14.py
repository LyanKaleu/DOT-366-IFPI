from random import randint


max_lista = 10

def gerar_lista(tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(randint(-1000, 1000))
    return lista


def trocar_valor_negativo(lista):
    for i in range(len(lista)):
        if lista[i] < 0:
            lista[i] = 0
    return lista


def main():
    C = gerar_lista(max_lista)

    print(f'Antes da troca: {C}')
    C = trocar_valor_negativo(C)
    print(f'Depois da troca: {C}')


if __name__ == '__main__':
    main()
