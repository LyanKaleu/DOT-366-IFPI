def eh_perfeito(n):
    if type(n) != int or n <= 0:
        return Exception
    
    if n == 1:
        return False

    soma = 1

    for i in range(2, n):
        if n % i == 0:
            soma += i


    if soma == n:
        return True
    else:
        return False


# Valores válidos
assert eh_perfeito(6) == True
assert eh_perfeito(28) == True
assert eh_perfeito(20) == False
assert eh_perfeito(1) == False

# Valores inválidos
assert eh_perfeito(-1) == Exception
assert eh_perfeito(2.5) == Exception
assert eh_perfeito('palavra') == Exception



print("Passou todos os testes!")
