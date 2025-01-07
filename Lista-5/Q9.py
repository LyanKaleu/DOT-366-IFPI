def eliminar_valores_repetidos(lista):
    if type(lista) != list or len(lista) == 0:
        return Exception

    nova_lista = []

    for i in lista:
        if type(i) != int:
            return Exception

        if lista.count(i) > 1:
            continue
        else:
            nova_lista.append(i)
    
    return nova_lista


# Valores válidos
assert eliminar_valores_repetidos([5, 4, 5, 7, 3, 4]) == [7, 3]
assert eliminar_valores_repetidos([1, 1, 1, 1]) == []
assert eliminar_valores_repetidos([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert eliminar_valores_repetidos([1, 1, 1, 2, 3, 3, 3, 4]) == [2, 4]

# Valores inválidos
assert eliminar_valores_repetidos([]) == Exception
assert eliminar_valores_repetidos([1.2, 1.1, 1.2]) == Exception
assert eliminar_valores_repetidos(['5', '4', '5', '7']) == Exception
assert eliminar_valores_repetidos(10) == Exception

print("Passou em todos os testes!")
