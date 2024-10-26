from random import randint

alternativas = ['A', 'B', 'C', 'D', 'E']
max_lista = 30
numero_alunos = 10

def gerar_gabarito(tamanho):
    lista = []
    for i in range(tamanho):
        resposta = alternativas[randint(0, 4)]
        lista.append(resposta)
    return lista


def gerar_cartao_resposta(tamanho):
    cartao = []
    for i in range(tamanho):
        alternativa = alternativas[randint(0, 4)]
        cartao.append(alternativa)
    return cartao


def verificar_acertos(gabarito, resposta_aluno):
    return gabarito == resposta_aluno


def calcular_acertos(gabarito, cartao_resposta):
    acertos = 0

    for i in range(len(gabarito)):
        if verificar_acertos(gabarito[i], cartao_resposta[i]):
            acertos += 1

    return acertos


def main():
    gabarito = gerar_gabarito(max_lista)

    print("-=" * 50)
    print("\n\n")
    print('Gabarito:')
    for i in range(max_lista):
        print(f'{i+1}){gabarito[i]}', end=" ")

    print("\n\n")
    print("-=" * 50)
    print("\n\n")
    print('Cartões de resposta:')
    for aluno in range(numero_alunos):
        print(f'Aluno {aluno+1}:')
        cartao_resposta = gerar_cartao_resposta(max_lista)
        for i in range(max_lista):
            print(f'{i+1}){cartao_resposta[i]}', end=" ")
        acertos = calcular_acertos(gabarito, cartao_resposta)
        print(f"\nN° acertos: {acertos}")
        print('\n\n')


if __name__ == '__main__':
    main()
