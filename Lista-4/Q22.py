def somatorio_fracionario_fatorial(n):
    if type(n) != int or n < 0:
        return Exception
    

    def fatorial(x):
        if x == 0 or x == 1:
            return 1
        
        f = 1

        for i in range(2, x + 1):
            f *= i
        
        return f

    soma = 0

    for i in range(n + 1):
        soma += (1 / fatorial(i))
    
    return round(soma, 2)


# Valores válidos
assert somatorio_fracionario_fatorial(0) == 1.00
assert somatorio_fracionario_fatorial(1) == 2.00
assert somatorio_fracionario_fatorial(2) == 2.50
assert somatorio_fracionario_fatorial(3) == 2.67
assert somatorio_fracionario_fatorial(4) == 2.71
assert somatorio_fracionario_fatorial(5) == 2.72

# Valores inválidos
assert somatorio_fracionario_fatorial(-1) == Exception
assert somatorio_fracionario_fatorial(3.5) == Exception
assert somatorio_fracionario_fatorial("5") == Exception
assert somatorio_fracionario_fatorial(None) == Exception

print("Todos os testes passaram!")
