def ordernar(n1, n2):
    if type(n1) != int or type(n2) != int:
        return Exception

    if n1 > n2:
        return (n2, n1)
    elif n2 > n1:
        return (n1, n2)
    else:
        return (n1, n2)


# Valores válidos
assert ordernar(1, 2) == (1, 2)
assert ordernar(5, 4) == (4, 5)
assert ordernar(10, 10) == (10, 10)
assert ordernar(64, -1) == (-1, 64)

# Valores inválidos
assert ordernar(1.2, 2) == Exception
assert ordernar(True, False) == Exception
assert ordernar('f', 'a') == Exception

print('Passou todos os testes!')
