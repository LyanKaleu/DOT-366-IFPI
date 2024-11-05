from random import randint


max_lista = 4


def gerar_lista(tamanho):
    lista = []
    for i in range(tamanho):
        numero = randint(1, 10)
        lista.append(numero)
    
    return lista


def produto_todos_outros_numeros(lista):
    nova_lista = []

    for i in range(len(lista)):
        produto = 1
        for j in range(len(lista)):
            if i != j:
                produto *= lista[j]
        nova_lista.append(produto)
    
    return nova_lista


def main():
    lista = gerar_lista(max_lista)
    print(f"Lista: {lista}")
    
    nova_lista = produto_todos_outros_numeros(lista)
    print(f"Lista de elementos do produto de outros números: {nova_lista}")


if __name__ == '__main__':
    main()
