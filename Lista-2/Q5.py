max_lista = 10

def ler_lista(tamanho):
    lista = []
    while True:
        try:
            for i in range(tamanho):
                lista.append(int(input(f'Digite o {i+1}º número: ')))
            break
        except ValueError:
            print('Digite apenas números inteiros.')
    return lista

def intercalar_listas(lista1, lista2):
    lista_intercalada = []
    for i in range(len(lista1)):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])
    return lista_intercalada

def main():
    print('-=' * 20)
    print('1ª Lista')
    lista1 = ler_lista(max_lista)
    print('-=' * 20)
    print('2ª Lista')
    lista2 = ler_lista(max_lista)
    lista_intercalada = intercalar_listas(lista1, lista2)

    print(f'\n\nLista 1: {lista1}\n\n')
    print(f'Lista 2: {lista2}\n\n')
    print(f'Lista intercalada: {lista_intercalada}\n\n')


if __name__ == '__main__':
    main()
