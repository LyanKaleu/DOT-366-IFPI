def maior_e_menor(lista):
    if type(lista) != list or len(lista) != 50:
        return Exception
    
    for n in lista:
        if type(n) != int:
            return Exception

    maior = menor = 0

    for numero in lista:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero
    
    return maior, menor


# Valores válidos
assert maior_e_menor([36, 16, 37, 18, 79, -25, 44, 5, 76, 97, -23, 14, 53, -7, 82, -2, -39, -19, -6, 95, 48, -41, -43, 1, 81, -27, 86, 3, -21, -19, 22, -16, 55, -45, -27, 68, 85, 80, 67, 93, 52, 89, 23, 85, -14, -5, 56, 64, 60, 47]) == (97, -45)

# Valores inválidos
assert maior_e_menor([]) == Exception
assert maior_e_menor('teste') == Exception
assert maior_e_menor([2.5, 3.5, 4.5]) == Exception
assert maior_e_menor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == Exception


print("Passou todos os testes!")
