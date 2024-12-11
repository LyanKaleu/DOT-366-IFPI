def tipo_triangulo(x, y, z):
    if (type(x) != int and type(x) != float) or (type(y) != int and type(y) != float) or (type(z) != int and type(z) != float):
        return Exception
    
    if (x <= 0) or (y <= 0) or (z <= 0):
        return Exception

    if (x < y + z) and (y < x + z) and (z < x + y):
        if (x == y) and (y == z):
            return 'Triângulo Equilátero'
        elif (x == y) or (y == z) or (x == z):
            return 'Triângulo Isósceles'
        else:
            return 'Triângulo Escaleno'
    else:
        return 'Não forma triângulo'


# Valores válidos
assert tipo_triangulo(3, 4, 5) == 'Triângulo Escaleno'
assert tipo_triangulo(3, 3, 3) == 'Triângulo Equilátero'
assert tipo_triangulo(9, 5, 5) == 'Triângulo Isósceles'
assert tipo_triangulo(24, 3, 2) == 'Não forma triângulo'
assert tipo_triangulo(2.5, 6, 7) == 'Triângulo Escaleno'

# Valores inválidos
assert tipo_triangulo(-1, -3, -5) == Exception
assert tipo_triangulo('A', 'B', 'C') == Exception


print("Passou todos os testes!")
