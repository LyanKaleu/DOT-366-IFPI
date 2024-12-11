def potencia(X, Z):
    if type(X) != int or type(Z) != int:
        return Exception

    if Z < 0:
        return Exception
    
    resultado = 1

    for _ in range(Z):
        resultado *= X
    
    return resultado


# Valores válidos
assert potencia(2, 3) == 8
assert potencia(5, 4) == 625
assert potencia(3, 0) == 1

# Valores inválidos
assert potencia(2, -3) == Exception
assert potencia(2.5, 5.9) == Exception
assert potencia(True, None) == Exception

print("Todos os testes passaram!")
