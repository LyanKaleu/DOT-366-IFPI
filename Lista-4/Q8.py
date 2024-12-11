def eh_positivo(n):
    if type(n) != int:
        return Exception

    return n > 0


# Valores válidos
assert eh_positivo(2) == True
assert eh_positivo(0) == False
assert eh_positivo(-1) == False
 
# Valores inválidos
assert eh_positivo(1.5) == Exception
assert eh_positivo(-9.7) == Exception
assert eh_positivo('palavra') == Exception


print("Passou todos os testes!")
