from random import randint


max_lista = 10


def gerar_listar(tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(randint(1, 100))

    return lista


def contar_elemento(elemento, lista):
    contador = 0

    for i in range(len(lista)):
        if lista[i] == elemento:
            contador += 1

    return contador


def determinar_indice(elemento, lista):
    indices = []

    for i in range(len(lista)):
        if lista[i] == elemento:
            indices.append(i)

    return indices


def main():
    W = gerar_listar(max_lista)
    print(f'Lista W: {W}')

    while True:
        try:
            V = int(input("Digite o elemento que deseja contar: "))
            quantidade = contar_elemento(V, W)
            posicoes = determinar_indice(V, W)

            if quantidade == 0:
                print(f'O elemento {V} não aparece na lista W.')
            elif quantidade > 1:
                print(f'O elemento {V} aparece {quantidade} vezes.')
            else:
                print(f"O elemento {V} aparece {quantidade} vez.")
            
            if len(posicoes) > 1:
                print(f'As posições do elemento {V} na lista W são: {posicoes}')
            elif len(posicoes) == 1:
                print(f'A posição do elemento {V} na lista W é: {posicoes[0]}')
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
            continue



if __name__ == '__main__':
    main()
