def soma_cumulativa(lista):
    if type(lista) != list or len(lista) == 0:
        return Exception
    
    nova_lista = []
    soma = 0

    for i in lista:
        if type(i) != int:
            return Exception
        
        soma += i
        nova_lista.append(soma)


    return nova_lista


# Valores válidos
assert soma_cumulativa([1, 2, 3]) == [1, 3, 6]
assert soma_cumulativa([10]) == [10]
assert soma_cumulativa([-9, -2, 3, 4]) == [-9, -11, -8, -4]
assert soma_cumulativa([-1, 1]) == [-1, 0]

# Valores inválidos
assert soma_cumulativa([]) == Exception
assert soma_cumulativa([1.1, 1.3, 1.5]) == Exception
assert soma_cumulativa(['teste']) == Exception
assert soma_cumulativa('teste') == Exception
# assert soma_cumulativa() == Exception
# assert soma_cumulativa(1, 2, 3) == Exception
# PERGUNTAR PRO PROF!


print("Passou em todos os testes!")
