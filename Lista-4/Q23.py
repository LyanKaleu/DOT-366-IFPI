def somatorio(n):
    if type(n) != int or n <= 0:
        return Exception
    
    soma = 0

    for i in range(1, n + 1):
        soma += ((i ** 2 + 1) / (i + 3))

    return round(soma, 1)


# Valores válidos
assert somatorio(2) == 1.5
assert somatorio(3) == 3.2
assert somatorio(1) == 0.5

# Valores inválidos

assert somatorio(0) == Exception
assert somatorio(-1) == Exception
assert somatorio(3.2) == Exception
assert somatorio("10") == Exception
assert somatorio(True) == Exception

print("Todos os testes passaram!")
