def gerar_lista(tamanho):
    lista = []
    for i in range(tamanho):
        lista.append("")
    
    return lista


def verificar_entrada():
    try:
        r = int(input("Digite o tamanho da lista: "))
        if r <= 0:
            print("Tamanho inválido! Tente novamente.")
            return verificar_entrada()
        return r
    except ValueError:
        print("Tamanho inválido! Tente novamente.")
        return verificar_entrada()


def menu():
    print("\n\n")
    print("===== MENU =====")
    print("1) Cadastrar nome")
    print("2) Pesquisar nome")
    print("3) Listar todos os nomes")
    print("0) Sair do programa")
    print("----------------")


def selecionar_opcao():
    while True:
        try:
            opcao = int(input("Digite sua escolha:_"))
            if opcao < 0 or opcao > 3:
                raise ValueError("Opção inválida!")
            return opcao
        except ValueError as e:
            print(e)
            print("Digite uma opção válida.")


def cadastrar_nome(lista):
    while True:
        try:
            nome = input("Digite o nome a ser cadastrado: ")
            if not all(c.isalpha() or c.isspace() for c in nome):
                raise ValueError("ERRO! O nome deve conter apenas letras alfabéticas e espaços.")
            if nome in lista:
                print(f"ERRO! '{nome}' já está cadastrado!")
            else:
                for i in range(len(lista)):
                    if lista[i] == "":
                        lista[i] = nome
                        print(f"Nome '{nome}' cadastrado com sucesso!")
                        return
                else:
                    print("ERRO! A lista está cheia.")
                    return
        except ValueError as e:
            print(e)

   


def pesquisar_nome(lista):
    if all(nome == "" for nome in lista):
        print("ERRO! Nenhum nome cadastrado!")
        return
    while True:
        try:
            nome = input("Digite o nome a ser pesquisado: ")
            if not all(c.isalpha() or c.isspace() for c in nome):
                raise ValueError("ERRO! O nome deve conter apenas letras alfabéticas e espaços.")
            if nome in lista:
                print(f"Nome '{nome}' encontrado!")
            else:
                print(f"ERRO! Nome '{nome}' não encontrado!")
            return
        except ValueError as e:
            print(e)


def listar_nomes(lista):
    if all(nome == "" for nome in lista):
        print("ERRO! Nenhum nome cadastrado!")
    else:
        print("Nomes cadastrados:")
        for nome in lista:
            if nome!= "":
                print(f'-> {nome}')


def main():
    tamanho = verificar_entrada()
    lista_nomes = gerar_lista(tamanho)

    while True:
        menu()
        opcao = selecionar_opcao()
        
        if opcao == 0:
            print("Programa encerrado!")
            break
        elif opcao == 1:
            cadastrar_nome(lista_nomes)
        elif opcao == 2:
            pesquisar_nome(lista_nomes)
        elif opcao == 3:
            listar_nomes(lista_nomes)
        


if __name__ == '__main__':
    main()
