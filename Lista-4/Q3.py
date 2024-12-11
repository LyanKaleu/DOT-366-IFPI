def eh_primo(n):
    if type(n) != int or n <= 0:
        return Exception

    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True


# Valores válidos
assert eh_primo(2) == True
assert eh_primo(13) == True
assert eh_primo(1) == False
assert eh_primo(100) == False

# Valores inválidos
assert eh_primo(0) == Exception
assert eh_primo(-3) == Exception
assert eh_primo(2.5) == Exception
assert eh_primo('palavra') == Exception


print("Passou todos os testes!")
