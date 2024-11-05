def somar_numeros_pares(lista):
    soma = 0
    
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    
    return soma


def main():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f'A soma dos números pares de 1 a 10 é {somar_numeros_pares(numeros)}')



if __name__ == '__main__':
    main()
