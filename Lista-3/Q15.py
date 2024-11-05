from random import randint


max_lista = 10


def gerar_lista(tamanho):
    lista = []
    for i in range(tamanho):
        numero = randint(1, 10)
        lista.append(numero)
    
    return lista


def frequencia_elemento(lista, numero):
    contador = 0

    for elemento in lista:
        if elemento == numero:
            contador += 1
    
    return contador


def lista_tuplas_frequencia(lista):
    frequencia_elementos = []
    elementos_adicionados = []
    for elemento in lista:
        if elemento not in elementos_adicionados:
            frequencia = frequencia_elemento(lista, elemento)
            frequencia_elementos.append((elemento, frequencia))
            elementos_adicionados.append(elemento)
    
    return frequencia_elementos


def ordernar_por_frequencia(lista_tuplas):
    for elemento in lista_tuplas:
        for i in range(len(lista_tuplas) - 1):
            if lista_tuplas[i][1] < lista_tuplas[i + 1][1]:
                lista_tuplas[i], lista_tuplas[i + 1] = lista_tuplas[i + 1], lista_tuplas[i]
    
    return lista_tuplas


def main():
    lista = gerar_lista(max_lista)
    print(f"Lista: {lista}")

    print("\nFrequência dos elementos:")
    frequencia_elementos = ordernar_por_frequencia(lista_tuplas_frequencia(lista)) 
    print(frequencia_elementos)  


if __name__ == '__main__':
    main()
