from random import randint


max_lista = 10


def gerar_lista(tamanho):
    lista = []
    for i in range(tamanho):
        numero = randint(1, 100)
        lista.append(numero)
    
    return lista


def determinar_maior_elemento(lista):
    maior = lista[0]

    for numero in lista:
        if numero > maior:
            maior = numero
    
    return maior


def determinar_menor_elemento(lista):
    menor = lista[0]

    for numero in lista:
        if numero < menor:
            menor = numero
    
    return menor


def menor_maior_diferenca(lista):
    menor = determinar_menor_elemento(lista)
    maior = determinar_maior_elemento(lista)

    return maior - menor


def main():
    lista = gerar_lista(max_lista)
    print(f'Números gerados: {lista}')
    print(f'\nMaior elemento: {determinar_maior_elemento(lista)}')
    print(f'Menor elemento: {determinar_menor_elemento(lista)}')
    print(f'Diferença entre maior e menor: {menor_maior_diferenca(lista)}')


if __name__ == '__main__':
    main()
