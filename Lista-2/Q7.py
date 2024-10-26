from random import randint

max_lista = 10

def gerar_lista(tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(randint(-50, 100))
    return lista


def esta_na_lista(lista):
    while True:
        try:
            numero = int(input('Digite um número inteiro: '))
            if numero in lista:
                return True
            return False
        except ValueError:
            print('Digite apenas números inteiros.')
    


def main():
    while True:
        numeros = gerar_lista(max_lista)
        print(f'Números gerados: {numeros}\n\n')

        if esta_na_lista(numeros):
            print('O número que você digitou está na lista')
        else:
            print('O número que você digitou não está na lista')
        
        print('\n\nDeseja continuar? [S/N]')
        continuar = input().strip().upper()
        if continuar == 'N':
            break
        elif continuar != 'S':
            print('Opção inválida! Digite novamente.')


if __name__ == "__main__":
    main()
