def lista_comeca_vogal(lista):
    vogais = ['a', 'e', 'i', 'o', 'u']
    nova_lista = []

    for palavra in lista:
        if palavra[0].lower() in vogais:
            nova_lista.append(palavra)
    
    return nova_lista


def main():
    palavras = ["gato", "elefante", "urso", "abelha", "cobra"]
    print(f"Palavras: {palavras}")
    print(f"Palavras que começam com vogal: {lista_comeca_vogal(palavras)}")



if __name__ == '__main__':
    main()
