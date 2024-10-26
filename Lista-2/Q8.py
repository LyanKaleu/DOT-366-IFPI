def contar_letra_A(frase):
    contador = 0
    for letra in frase:
        if letra.upper() == 'A':
            contador += 1
    return contador


def eh_letra(letra):
    return letra.isalpha() or letra.isspace()


def validar_entrada(frase):
    for letra in frase:
        if not eh_letra(letra):
            return False
    return True


def main():
    while True:
        try:
            entrada = input("Digite uma frase (ou 'sair' para encerrar): ")

            if entrada.lower() == 'sair':
                break

            if validar_entrada(entrada):
                frase_sem_espacos = entrada.replace(" ", "")
                quantidade_A = contar_letra_A(frase_sem_espacos)
                print(f"A letra 'A' aparece {quantidade_A} vezes na frase.")
            else:
                print("A frase deve conter somente letras do alfabeto e espaços.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    main()
