def somatorio_fracionario(n):
    if type(n) != int or n  <= 0:
        return Exception
    
    soma = 0

    for i in range(1, n + 1):
        soma += (1 / i)

    return round(soma, 2)


# Valores válidos
assert somatorio_fracionario(2) == 1.50
assert somatorio_fracionario(6) == 2.45
assert somatorio_fracionario(10) == 2.93

# Valores inválidos
assert somatorio_fracionario(0) == Exception
assert somatorio_fracionario(-1) == Exception
assert somatorio_fracionario(3.5) == Exception
assert somatorio_fracionario("5") == Exception
assert somatorio_fracionario(None) == Exception

print("Todos os testes passaram!")
