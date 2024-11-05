def determinar_maior(lista):
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero

    return maior


def determinar_menor(lista):
    menor = lista[0]
    for numero in lista:
        if numero < menor:
            menor = numero
    
    return menor


def main():
    notas = [7.5, 8.0, 9.0, 4.5, 6.0, 10.0, 5.0]
    print(f"Notas: {notas}")
    print(f"Maior nota: {determinar_maior(notas)}")
    print(f"Menor nota: {determinar_menor(notas)}")



if __name__ == "__main__":
    main()
