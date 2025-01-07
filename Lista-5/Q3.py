def maior_soma(lista):
    if type(lista) != list or len(lista) == 0:
        return Exception
    
    for num in lista:
        if type(num) != int:
            return Exception
    
    maior_soma = float('-inf') # Inicializa a maior soma com o menor valor possível

    for i in range(len(lista) - 1):
        soma_atual = lista[i] + lista[i + 1]
        if soma_atual > maior_soma:
            maior_soma = soma_atual
        
    return maior_soma


# Valores válidos
assert maior_soma([5,-2,-2,-7,3,15,10,-3,9,-6,4,1]) == 25
assert maior_soma([5,4,5,7,3,4]) == 12
assert maior_soma([1,3,4,4,4]) == 8
assert maior_soma([-1,-2,-3,-4]) == -3
assert maior_soma([1,2]) == 3
assert maior_soma([0,0,0,0]) == 0

# Valores inválidos
assert maior_soma(1) == Exception
assert maior_soma([1.1, 2.5, 1.1]) == Exception
assert maior_soma([]) == Exception
assert maior_soma(['a', 'b', 'c', 'a']) == Exception

print("Passou em todos os testes!")
