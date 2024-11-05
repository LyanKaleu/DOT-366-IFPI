tamanho = 5

def filtrar_tamanho(lista, tamanho):
    contador = 0

    for nome in lista:
        if len(nome) > tamanho:
            contador += 1
    
    return contador


def main():
    nomes = ["Ana", "Beatriz", "Carlos", "Daniel", "Eduarda", "Fabio"]
    print(f"Existem {filtrar_tamanho(nomes, tamanho)} nomes com mais de {tamanho} letras")


if __name__ == '__main__':
    main()
