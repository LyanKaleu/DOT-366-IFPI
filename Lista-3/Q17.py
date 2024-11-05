from random import randint


def gerar_matriz(x, y):
    matriz = []
    for i in range(x):
        linha = []
        for j in range(y):
            numero = randint(1, 10)
            linha.append(numero)
        matriz.append(linha)
    
    return matriz


def gerar_matriz_transposta(matriz):
    transposta = []
    for j in range(len(matriz[0])):
        coluna = []
        for i in range(len(matriz)):
            coluna.append(matriz[i][j])
        transposta.append(coluna)
    
    return transposta


def main():
    matriz_original = gerar_matriz(2, 3)
    print(f"Matriz original: {matriz_original}")

    matriz_transposta = gerar_matriz_transposta(matriz_original)
    print(f"Matriz transposta: {matriz_transposta}")



if __name__ == "__main__":
    main()
