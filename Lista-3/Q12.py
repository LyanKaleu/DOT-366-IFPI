from random import randint


def gerar_lista(tamanho):
    lista = []
    for i in range(tamanho):
        numero = randint(1, 25)
        lista.append(numero)
    
    return lista


def filtrar_lista_por_soma(lista):
    nova_lista = []

    for i in range(len(lista)):
        for j in range(len(lista)):
            for k in range(len(lista)):
                if i != j and lista[i] == lista[j] + lista[k]:
                    nova_lista.append(lista[i])
    
    return list(set(nova_lista))


def main():
    lista = gerar_lista(5)
    print(f'Lista original: {lista}')
    
    lista_filtrada = filtrar_lista_por_soma(lista)
    print(f'Lista filtrada: {lista_filtrada}')



if __name__ == '__main__':
    main()
