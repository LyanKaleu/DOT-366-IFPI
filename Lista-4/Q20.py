def somatorio(n):
    if type(n) !=int or n <= 0:
        return Exception
    
    soma = 0

    for i in range(1, n + 1):
        soma += i

    return soma


# Valores válidos
assert somatorio(1) == 1
assert somatorio(3) == 6
assert somatorio(5) == 15
assert somatorio(10) == 55

# Valores inválidos
assert somatorio(0) == Exception
assert somatorio(-1) == Exception
assert somatorio(3.5) == Exception
assert somatorio("5") == Exception
assert somatorio(None) == Exception

print("Todos os teste passaram!")
