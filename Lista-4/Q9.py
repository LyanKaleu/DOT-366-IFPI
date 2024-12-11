def eh_par(n):
    if type(n) != int:
        return Exception

    return n % 2 == 0


# Valores válidos
assert eh_par(10) == True
assert eh_par(1) == False
assert eh_par(0) == True
assert eh_par(-4) == True

# Valores inválidos
assert eh_par(1.2) == Exception
assert eh_par('palavra') == Exception
assert eh_par([2]) == Exception


print("Passou todos os testes!")
