def verificar_repeticao(lista):
    if type(lista) != list or len(lista) == 0:
        return Exception
    

    for i in lista:
        if type(i) != int:
            return Exception
        
        if lista.count(i) > 1:
            return True
        else:
            return False
        


# Valores válidos
assert verificar_repeticao([1, 2, 3, 1]) == True
assert verificar_repeticao([3, 7, 2, 4]) == False
assert verificar_repeticao([1]) == False
assert verificar_repeticao([1, 1, 1]) == True
assert verificar_repeticao([10, 100, 1000, 10000]) == False

# Valores inválidos
assert verificar_repeticao(1) == Exception
assert verificar_repeticao([1.1, 2.5, 1.1]) == Exception
assert verificar_repeticao([]) == Exception
assert verificar_repeticao(['1', '1', '1', '1']) == Exception

print("Passou em todos os testes!")
