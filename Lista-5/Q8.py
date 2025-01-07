def determinar_valor_mais_proximo_media(lista):
    if type(lista) != list or len(lista) == 0:
        return Exception

    soma = 0
    tamanho = len(lista)

    for i in lista:
        if type(i) != float and type(i) != int:
            return Exception
    
        soma += i
    
    media = soma / tamanho

    valor_mais_proximo = lista[0]
    menor_diferenca = abs(lista[0] - media)

    for i in lista:
        diferenca = abs(i - media)
        if diferenca < menor_diferenca:
            menor_diferenca = diferenca
            valor_mais_proximo = i
    
    return valor_mais_proximo


# Valores válidos
assert determinar_valor_mais_proximo_media([2.5, 7.5, 10.0, 4.0]) == 7.5
assert determinar_valor_mais_proximo_media([1, 2, 3, 4, 5]) == 3
assert determinar_valor_mais_proximo_media([6.8, 9.0, 9.2, 9.4]) == 9.0
assert determinar_valor_mais_proximo_media([5]) == 5

# Valores inválidos
assert determinar_valor_mais_proximo_media(['1.1', '1.5']) == Exception
assert determinar_valor_mais_proximo_media([]) == Exception
assert determinar_valor_mais_proximo_media(10) == Exception

print("Passou em todos os testes!")
