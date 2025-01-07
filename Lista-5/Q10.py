def maior_soma_repetidos(lista):
    if type(lista) != list or len(lista) == 0:
        return Exception
    
    for i in lista:
        if type(i) != int:
            return Exception
        
    soma_repetidos = {}

    for num in lista:
        if num in soma_repetidos:
            soma_repetidos[num] += num
        else:
            soma_repetidos[num] = num
    
    maior_soma = 0

    for valor in soma_repetidos.values():
        if valor > maior_soma:
            maior_soma = valor

    return maior_soma


# Valores válidos
assert maior_soma_repetidos([5, -2, -2, 5, 3, 5, 10, -2, 3, 10, 3, 1]) == 20
assert maior_soma_repetidos([1, 1, 1, 2, 3, 3, 3, 4, 4, 1, 5]) == 9
assert maior_soma_repetidos([1, 1, 1, 1]) == 4

# Valores inválidos
assert maior_soma_repetidos([]) == Exception
assert maior_soma_repetidos([1.2, 1.1, 1.2]) == Exception
assert maior_soma_repetidos(['5', '4', '5', '7']) == Exception
assert maior_soma_repetidos(10) == Exception

print("Passou em todos os testes!")
