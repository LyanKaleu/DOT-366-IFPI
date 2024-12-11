def divisores(n):
    if type(n) != int or n <= 0:
        return Exception

    divisores = 0

    for num in range(1, n + 1):
        if n % num == 0:
            divisores+=1
    
    return divisores


# Valores válidos
assert divisores(6) == 4
assert divisores(13) == 2
assert divisores(18) == 6
assert divisores(1) == 1

# Valores inválidos
assert divisores(0) == Exception
assert divisores(3.1) == Exception
assert divisores('3') == Exception
assert divisores(-5) == Exception


print("Todos os teste passaram!")
