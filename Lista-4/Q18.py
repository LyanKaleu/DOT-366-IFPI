def tabuada(n):
    if type(n) != int or n <= 0:
        return Exception
    
    resultado = []

    for i in range(1, n + 1):
        resultado.append(f'{i} x {n} = {i * n}')

    return resultado


# Valores válidos
assert tabuada(1) == ['1 x 1 = 1']
assert tabuada(3) == ['1 x 3 = 3', '2 x 3 = 6', '3 x 3 = 9']
assert tabuada(5) == ['1 x 5 = 5', '2 x 5 = 10', '3 x 5 = 15', '4 x 5 = 20', '5 x 5 = 25']

# Valores inválidos
assert tabuada(-1) == Exception
assert tabuada(0) == Exception
assert tabuada(3.5) == Exception
assert tabuada("5") == Exception
assert tabuada(None) == Exception

print("Todos os teste passaram!")
