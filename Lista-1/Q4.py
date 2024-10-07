def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2

    if media >= 6:
        return f'Média: {media:.1f}\nPARABÉNS! Você foi aprovado!'
    else:
        return f'Média: {media:.1f}\nVocê foi reprovado!'


def main():
    n1 = float(input('Digite a nota da primeira avaliação: '))
    n2 = float(input('Digite a nota da segunda avaliação: '))
    resultado = calcular_media(n1, n2)
    print(resultado)


if __name__ == '__main__':
    main()
