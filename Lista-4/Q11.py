def peso_ideal(altura, sexo):
    if type(altura) != float or altura < 0 or altura > 2.50:
        return Exception
    
    if type(sexo) != str or sexo not in ['m', 'M', 'f', 'F']:
        return Exception
    

    if sexo.upper() == 'M':
        return round(72.7 * altura - 58, 2)
    
    if sexo.upper() == 'F':
        return round(62.1 * altura - 44.7, 2)


# Valores válidos
assert peso_ideal(1.71, 'm') == 66.32
assert peso_ideal(2.10, 'm') == 94.67
assert peso_ideal(1.68, 'F') == 59.63

# Valores inválidos
assert peso_ideal(3, 'feminino') == Exception
assert peso_ideal(-1, 2) == Exception

print("Passou todos os testes!")
