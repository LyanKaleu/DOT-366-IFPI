def verificar_ordem_crescente(lista):
    if type(lista) != list or len(lista) == 0:
        return Exception
    
    for i in lista:
        if type(i) != int:
            return Exception

    ordenada = False

    for num in range(len(lista) - 1):
        if lista[num] <= lista[num + 1]:
            ordenada = True
        else:
            ordenada = False
            break
    
    return ordenada


# Valores válidos
assert verificar_ordem_crescente([1, 2, 3]) == True
assert verificar_ordem_crescente([3, 7, 2]) == False
assert verificar_ordem_crescente([1, 1, 1]) == True
assert verificar_ordem_crescente([-5, -4, 0]) == True
assert verificar_ordem_crescente([1, 0, -1, -2]) == False

# Valores inválidos
assert verificar_ordem_crescente([]) == Exception
assert verificar_ordem_crescente(['1', '2', '3']) == Exception
assert verificar_ordem_crescente((1, 2, 3)) == Exception

print("Passou em todos os testes!")
