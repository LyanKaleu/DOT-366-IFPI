from random import randint

max_lista = 15

def gravar_lista(tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(randint(-1000, 1000))
    return lista

def maior_elemento(numeros):
    maior = numeros[0]
    for i in numeros:
        if i > maior:
            maior = i
    return maior, numeros.index(maior)

def menor_elemento(numeros):
    menor = numeros[0]
    for i in numeros:
        if i < menor:
            menor = i
    return menor, numeros.index(menor)

def main():
    numeros = gravar_lista(max_lista)
    print(f'Números gerados: {numeros}\n\n')

    maior, index_maior = maior_elemento(numeros)
    print(f'Maior elemento: {maior} na posição {index_maior}\n\n')

    menor, index_menor = menor_elemento(numeros)
    print(f'Menor elemento: {menor} na posição {index_menor}\n\n')


if __name__ == '__main__':
    main()
