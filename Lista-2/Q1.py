from random import randint

max_lista = 100

def gravar_lista(tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(randint(-1000, 1000))
    return lista

def count_par(numeros):
    count = 0
    for i in numeros:
        if i % 2 == 0:
            count += 1
    return count

def lista_par(numeros):
    lista = []
    for i in numeros:
        if i % 2 == 0:
            lista.append(i)
    return lista

def count_impar(numeros):
    count = 0
    for i in numeros:
        if i % 2 != 0:
            count += 1
    return count

def lista_impar(numeros):
    lista = []
    for i in numeros:
        if i % 2 != 0:
            lista.append(i)
    return lista

def main():
    numeros = gravar_lista(max_lista)

    print(f'Números gerados: {numeros}\n\n')

    print(f'Quantidade de números pares: {count_par(numeros)}\n\n')
    print(f'Números pares: {lista_par(numeros)}\n\n')
    print(f'Quantidade de números ímpares: {count_impar(numeros)}\n\n')
    print(f'Números ímpares: {lista_impar(numeros)}\n\n')


if __name__ == '__main__':
    main()
