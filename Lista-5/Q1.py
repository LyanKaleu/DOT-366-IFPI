def remover_repeticoes(lista):
    if type(lista) != list or len(lista) == 0:
        return Exception
    
    for num in lista:
        if type(num) != int:
            return Exception

    nova_lista = []

    for num in lista:
        if num not in nova_lista:
            nova_lista.append(num)          
        
    return nova_lista


# Valores válidos
assert remover_repeticoes([5,4,5,7,3,4]) == [5,4,7,3]
assert remover_repeticoes([1,2,3,4,5,6,7,8,9]) == [1,2,3,4,5,6,7,8,9]
assert remover_repeticoes([1,1,1,1,1,1,1,1,1]) == [1]
assert remover_repeticoes([9,8,9,8,9,8,5,9,9]) == [9,8,5]

# Valores inválidos
assert remover_repeticoes(1) == Exception
assert remover_repeticoes([1.1, 2.5, 1.1]) == Exception
assert remover_repeticoes([]) == Exception
assert remover_repeticoes(['a', 'b', 'c', 'a']) == Exception

print("Passou em todos os testes!")
