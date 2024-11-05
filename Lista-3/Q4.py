from random import randint


max_lista = 10


def gerar_lista(tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(randint(1, 100))
    
    return lista


def maioridade(idade):
    if idade >= 18:
        return True
    else:
        return False
    

def dividir_lista(lista):
    lista_maioridade = []
    lista_menoridade = []
    
    for idade in lista:
        if maioridade(idade):
            lista_maioridade.append(idade)
        else:
            lista_menoridade.append(idade)
    
    return lista_maioridade, lista_menoridade


def main():
    idades = gerar_lista(max_lista)
    print(f"Idades geradas: {idades}")

    lista_maioridade, lista_menoridade = dividir_lista(idades)
    print(f"Idades maiores de 18: {lista_maioridade}")
    print(f"Idades menores de 18: {lista_menoridade}")


if __name__ == '__main__':
    main()
