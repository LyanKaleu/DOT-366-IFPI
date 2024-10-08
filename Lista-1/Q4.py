def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2

    if media >= 6:
        return f'Média: {media:.1f}\nPARABÉNS! Você foi aprovado!'
    else:
        return f'Média: {media:.1f}\nVocê foi reprovado!'


def main():
    while True:
        try:
            n1 = float(input('Digite a nota da primeira avaliação: '))
            if n1 < 0 or n1 > 10:
                print('Nota inválida! Digite um valor entre 0 e 10.')
                continue
            n2 = float(input('Digite a nota da segunda avaliação: '))
            if n2 < 0 or n2 > 10:
                print('Nota inválida! Digite um valor entre 0 e 10.')
                continue
            resultado = calcular_media(n1, n2)
            print(resultado)
            break
        except ValueError:
            continue


if __name__ == '__main__':
    main()
