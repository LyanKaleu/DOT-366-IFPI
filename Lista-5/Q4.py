def maior_soma_por_segmento(lista):
    if type(lista) != list or len(lista) == 0:
        return Exception
    
    for num in lista:
        if type(num) != int:
            return Exception
        
    maior_soma = float('-inf')
    soma_atual = 0

    for num in lista:
        soma_atual = max(num, soma_atual + num)
        maior_soma = max(maior_soma, soma_atual)
    
    return maior_soma


# Valores válidos
assert maior_soma_por_segmento([5,-2,-2,-7,3,15,10,-3,9,-6,4,1]) == 34
assert maior_soma_por_segmento([5,4,5,7,3,4]) == 28
assert maior_soma_por_segmento([1,3,4,4,4]) == 16
assert maior_soma_por_segmento([-1,-2,-3,-4]) == -1
assert maior_soma_por_segmento([1,2]) == 3
assert maior_soma_por_segmento([0,0,0,0]) == 0

# Valores inválidos
assert maior_soma_por_segmento(1) == Exception
assert maior_soma_por_segmento([1.1, 2.5, 1.1]) == Exception
assert maior_soma_por_segmento([]) == Exception
assert maior_soma_por_segmento(['a', 'b', 'c', 'a']) == Exception

print("Passou em todos os testes!")
