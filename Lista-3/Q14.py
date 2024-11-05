from random import randint


def gerar_matriz(n):
    matriz = []
    
    for i in range(n):
        linha = []
        for j in range(n):
            numero = randint(1, 10)
            linha.append(numero)
        matriz.append(linha)
    
    return matriz


def somar_elementos_linha(linha):
    soma = 0

    for numero in linha:
        soma += numero
    
    return soma


def main():
    matriz = gerar_matriz(3)
    print(f'Matriz: {matriz}')
    
    soma_elementos_linha = []
    
    for i in range(len(matriz)):
        soma_elementos_linha.append(somar_elementos_linha(matriz[i]))
    
    print(f'Soma dos elementos de cada linha: {soma_elementos_linha}')


if __name__ == '__main__':
    main()
