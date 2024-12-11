def calcular_media(nota1, nota2, nota3, letra):
    notas = [nota1, nota2, nota3] 
    
    if type(letra) != str:
        return Exception
    
    for nota in notas:
        if (nota < 0 and nota > 10) or type(nota) == str:
            return Exception

    if letra.upper() not in ['A', 'P']:
        return Exception

    if letra.upper() == 'A':
        return (nota1 + nota2 + nota3) / 3
    elif letra.upper() == 'P':
        return ((nota1 * 5) + (nota2 * 3) + (nota3 * 2) / 10)


# Valores válidos
assert calcular_media(7, 8.4, 9.2, 'A') == 8.2
assert calcular_media(6, 3, 3, 'a') == 4
assert calcular_media(10, 10, 10, 'b') == 10

# Valores inválidos
assert calcular_media(-3, 4, 4, 'A') == Exception
assert calcular_media(5, 11, 9, 'B') == Exception

print("Passou todos os testes!")
