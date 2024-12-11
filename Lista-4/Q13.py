def calcular_duracao(hora_inicio, hora_termino):
    # Validação dos parâmetros
    if type(hora_inicio) != tuple or type(hora_termino) != tuple:
        return Exception
    
    if len(hora_inicio) != 2 or len(hora_termino) != 2:
        return Exception
    
    if not (isinstance(hora_inicio[0], int) and isinstance(hora_inicio[1], int) and 
            isinstance(hora_termino[0], int) and isinstance(hora_termino[1], int)):
        return Exception
    
    if hora_inicio[0] < 0 or hora_inicio[0] > 23 or hora_inicio[1] < 0 or hora_inicio[1] > 59:
        return Exception
    
    if hora_termino[0] < 0 or hora_termino[0] > 23 or hora_termino[1] < 0 or hora_termino[1] > 59:
        return Exception
    
    # Converter horários para minutos totais
    minutos_inicio = hora_inicio[0] * 60 + hora_inicio[1]
    minutos_termino = hora_termino[0] * 60 + hora_termino[1]

    # Ajustar o caso em que o término ocorre no dia seguinte
    if minutos_termino < minutos_inicio:
        minutos_termino += 24 * 60

    # Calcular a diferença de minutos entre o término e o início
    duracao_total_minutos = minutos_termino - minutos_inicio

    # Conventer minutos totais em horas e minutos
    horas = duracao_total_minutos // 60
    minutos = duracao_total_minutos % 60

    return (horas, minutos)


# Valores válidos
assert calcular_duracao((0,0), (6,0)) == (6,0)
assert calcular_duracao((22,37), (3,31)) == (4,54)
assert calcular_duracao((14,0), (18,0)) == (4,0)
assert calcular_duracao((15,0), (15,45)) == (0,45)
assert calcular_duracao((12,0), (12,0)) == (0,0)
assert calcular_duracao((0,0), (23,59)) == (23,59)

# Valores inválidos
assert calcular_duracao((-3, 40), (21,65)) == Exception
assert calcular_duracao((12,0), (25,0)) == Exception
assert calcular_duracao((4.5, 0), (None, None)) == Exception
assert calcular_duracao(('12', '30'), ('8', '0')) == Exception


print("Passou todos os testes!")
