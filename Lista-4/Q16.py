def calcular_media(lista):
    if type(lista) != list or len(lista) == 0:
        return Exception


    soma = 0
    for i in range(len(lista)):
        if type(lista[i]) != int or lista[i] < 0:
            return Exception

        soma += lista[i]
    
    return soma / len(lista)


assert calcular_media([1,2,4,5]) == 3
assert calcular_media([1,1,1,1,1,1,1,1,1]) == 1
assert calcular_media([10]) == 10


assert calcular_media([10,5.4]) == Exception
assert calcular_media([-1]) == Exception
assert calcular_media([]) == Exception
assert calcular_media([-2,3]) == Exception
assert calcular_media(["*",5]) == Exception
assert calcular_media('teste') == Exception

print("Passou todos os testes!")
