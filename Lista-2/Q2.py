from random import uniform

max_lista = 10

def gravar_lista(tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(round(uniform(-100, 100), 2))
    return lista

def count_negativo(numeros):
    count = 0
    for i in numeros:
        if i < 0:
            count += 1
    return count

def soma_positivos(numeros):
    soma = 0
    for i in numeros:
        if i > 0:
            soma += i
    return soma


def main():
    numeros = gravar_lista(max_lista)
    print(f'Números gerados: {numeros}\n\n')

    print(f'Quantidade de números negativos: {count_negativo(numeros)}\n\n')

    print(f'Soma dos números positivos: {soma_positivos(numeros):.2f}\n\n')


if __name__ == '__main__':
    main()
