from random import randint


max_lista = 6


def gerar_lista(tamanho):
    lista = []
    for i in range(tamanho):
        numero = randint(1, 50)
        lista.append(numero)
    
    return lista


def determinar_paridade(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"
    

def agrupa_por_paridade(lista):
    pares = []
    impares = []
    
    for numero in lista:
        paridade = determinar_paridade(numero)
        if paridade == "par":
            pares.append(numero)
        else:
            impares.append(numero)
    
    return pares, impares


def main():
    lista = gerar_lista(max_lista)
    print(f"Lista: {lista}")
    
    pares, impares = agrupa_por_paridade(lista)
    lista_paridade = [pares, impares]
    
    print(f"-> Pares: {pares}")
    print(f"-> Ímpares: {impares}")
    print(f"-> Lista contendo ambas as paridades: {lista_paridade}")


if __name__ == "__main__":
    main()
