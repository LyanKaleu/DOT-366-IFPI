def ler_lista(tamanho):
    lista = []
    while True:
        try:
            for i in range(tamanho):
                lista.append(int(input(f"Digite o {i+1}º número: ")))
            break
        except ValueError:
            print("Digite apenas números inteiros.")

    return lista


def gerar_lista_de_outras_listas(x, y):
    lista = []

    for i in range(len(x)):
        lista.append(x[i])
    
    for j in range(len(y)):
        lista.append(y[j])
    
    return lista


def main():
    print("-=" * 20)
    print("Lista R:")
    R = ler_lista(5)
    
    print("\n\n")
    print("-=" * 20)
    print("Lista S:")
    S = ler_lista(10)

    print("\n\n")
    print("-=" * 20)
    print("Lista X:")
    nova_lista = gerar_lista_de_outras_listas(R, S)
    print(nova_lista)



if __name__ == '__main__':
    main()
