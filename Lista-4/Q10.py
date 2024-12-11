def determinar_conceito(media_final):
    if not isinstance(media_final, (float, int)) or media_final < 0 or media_final > 10:
        return Exception

    if 0 <= media_final <= 4.9:
        return 'D'
    elif 5 <= media_final <= 6.9:
        return 'C'
    elif 7 <= media_final <= 8.9:
        return 'B'
    else:
        return 'A'


# Valores válidos
assert determinar_conceito(0) == 'D'
assert determinar_conceito(3.5) == 'D'
assert determinar_conceito(5.0) == 'C'
assert determinar_conceito(6.9) == 'C'
assert determinar_conceito(7.5) == 'B'
assert determinar_conceito(9.2) == 'A'

# Valores inválidos
assert determinar_conceito(-1) == Exception
assert determinar_conceito(11) == Exception
assert determinar_conceito('palavra') == Exception

print("Passou todos os testes!")
