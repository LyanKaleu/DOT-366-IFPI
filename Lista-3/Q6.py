from random import randint


max_lista = 10


def gerar_lista(tamanho):
    lista = []
    for i in range(tamanho):
        numero = randint(1, 10)
        lista.append(numero)
    
    return lista


def remover_duplicatas(lista):
    lista_sem_duplicatas = []
    for numero in lista:
        if numero not in lista_sem_duplicatas:
            lista_sem_duplicatas.append(numero)
    
    return lista_sem_duplicatas


def main():
    numeros = gerar_lista(max_lista)
    print(f'Números gerados: {numeros}')
    print(f'\nNúmeros sem duplicatas: {remover_duplicatas(numeros)}')



if __name__ == '__main__':
    main()
