from random import randint, uniform

max_lista = 20

def gerar_quantidade_produtos(tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(randint(1, 6))
    return lista


def gerar_preco_produtos(tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(round(uniform(1, 500), 2))
    return lista


def calcular_faturamento(quantidade, preco):
    return quantidade * preco


def calcular_media(soma, quantidade):
    return soma / quantidade


def abaixo_da_media(numeros, media):
    count = 0
    for i in numeros:
        if i < media:
            count += 1
    return count


def main():
    quantidade = gerar_quantidade_produtos(max_lista)
    preco = gerar_preco_produtos(max_lista)
    faturamento_total = 0
    lista_faturamentos = []

    for i in range(max_lista):
        print(f'Produto {i + 1}: {quantidade[i]} unidades - R$ {preco[i]:.2f}')
        faturamento_produto = calcular_faturamento(quantidade[i], preco[i])
        print(f'Faturamento: {faturamento_produto:.2f}\n\n')
        lista_faturamentos.append(faturamento_produto)
        faturamento_total += faturamento_produto

    media = calcular_media(faturamento_total, max_lista)
    
    print(f'-> Faturamento total: R$ {faturamento_total:.2f}\n')
    print(f'-> Média de faturamento: R$ {media:.2f}\n')
    print(f'-> Quantidade de faturamentos abaixo da média: {abaixo_da_media(lista_faturamentos, media)}')
        
    

if __name__ == '__main__':
    main()
