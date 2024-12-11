def determinar_categoria(idade):
    if type(idade) != int or idade < 5 or idade >= 120:
        return Exception
    
    if 5 <= idade <= 7:
        return 'Infantil A'
    elif 8 <= idade <= 10:
        return 'Infantil B'
    elif 11 <= idade <= 13:
        return 'Juvenil A'
    elif 14 <= idade <= 17:
        return 'Juvenil B'
    else:
        return 'Adulto'


# Valores válidos
assert determinar_categoria(5) == 'Infantil A'
assert determinar_categoria(8) == 'Infantil B'
assert determinar_categoria(12) == 'Juvenil A'
assert determinar_categoria(17) == 'Juvenil B'
assert determinar_categoria(18) == 'Adulto'
assert determinar_categoria(60) == 'Adulto'


# Valores inválidos
assert determinar_categoria(3) == Exception
assert determinar_categoria(190) == Exception
assert determinar_categoria(5.6) == Exception
assert determinar_categoria('5 anos') == Exception


print("Passou todos os testes!")
