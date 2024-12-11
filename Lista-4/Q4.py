def converter_tempo(segundos):
    if type(segundos) == str or segundos <= 0:
        return Exception
    
    horas = segundos // 3600
    segundos %= 3600
    minutos = segundos // 60
    segundos %= 60

    return horas, minutos, segundos


# Valores válidos
assert converter_tempo(60) == (0, 1, 0)
assert converter_tempo(100) == (0, 1, 40)
assert converter_tempo(180) == (0, 3, 0)
assert converter_tempo(3600) == (1, 0, 0)
assert converter_tempo(172800) == (48, 0, 0)
assert converter_tempo(12.5) == (0, 0, 12.5)
assert converter_tempo(400.5) == (0, 6, 40.5)

# Valores inválidos
assert converter_tempo(-1) == Exception
assert converter_tempo('palavra') == Exception


print("Passou todos os testes!")
