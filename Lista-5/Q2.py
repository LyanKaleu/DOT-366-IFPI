def contar_elementos(lista):
    if type(lista) != list or len(lista) == 0:
        return Exception
    
    for num in lista:
        if type(num) != int:
            return Exception

    contagem = {}
    
    for num in lista:
        if num not in contagem:
            contagem[num] = 1
        else:
            contagem[num] += 1

    return contagem


# Valores válidos
assert contar_elementos([5,4,5,7,3,4]) == {5: 2, 4: 2, 7: 1, 3: 1}
assert contar_elementos([1,2,3,4,5,6,7,8,9]) == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
assert contar_elementos([1,1,1,1,1,1,1,1,1]) == {1: 9}
assert contar_elementos([9,8,9,8,9,8,5,9,9]) == {9: 5, 8: 3, 5: 1}

# Valores inválidos
assert contar_elementos(1) == Exception
assert contar_elementos([1.1, 2.5, 1.1]) == Exception
assert contar_elementos([]) == Exception
assert contar_elementos(['a', 'b', 'c', 'a']) == Exception

print("Passou em todos os testes!")
