from random import randint

faces = 6

def lancar_dado(vezes):
    resultados = []
    for _ in range(vezes):
        resultados.append(randint(1, 6))

    return resultados


def calcular_frequencia(face, resultados):
    numero_ocorrencias = 0
    for resultado in resultados:
        if resultado == face:
            numero_ocorrencias += 1

    return numero_ocorrencias



def main():
    while True:
        try:
            vezes = int(input("Digite o número de vezes que deseja lançar o dado: "))
            if vezes <= 0:
                print("O número de vezes deve ser um número inteiro e positivo.")
                continue
            resultados = lancar_dado(vezes)
            print("\n\nResultados dos lançamentos:")
            for i in range(len(resultados)):
                if i == len(resultados) - 1:
                    print(resultados[i])
                else:
                    print(resultados[i], end=" -> ")
            
            print("\n\nFrequências dos resultados:")
            for face in range(1, faces+1):
                frequencia = calcular_frequencia(face, resultados)
                print(f'Face {face}: {frequencia} vezes')
            
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
            continue


if __name__ == '__main__':
    main()
