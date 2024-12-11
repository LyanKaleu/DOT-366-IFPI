def fatorial(n):
    if type(n) != int or n < 0:
        return Exception
    
    resultado = 1

    if n == 0:
        return resultado

    for i in range(n, 0, -1):
        resultado *= i

    return resultado


# Valores válidos
assert fatorial(0) == 1 
assert fatorial(1) == 1
assert fatorial(5) == 120 
assert fatorial(7) == 5040 

# Valores inválidos
assert fatorial(-1) == Exception
assert fatorial(3.5) == Exception
assert fatorial('6') == Exception

print("Todos os testes passaram!")
