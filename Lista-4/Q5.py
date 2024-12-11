def idade_em_dias(anos, meses, dias):
    if type(anos or meses or dias) != int or meses > 12:
        return Exception

    anos += meses // 12
    meses %= 12

    return (anos * 365) + (meses * 30) + dias


# Valores válidos
assert idade_em_dias(1, 0, 0) == 365
assert idade_em_dias(25, 4, 15) == 9260
assert idade_em_dias(20, 12, 11) == 7676

# Valores inválidos
assert idade_em_dias(1.2, -9, 7) == Exception
assert idade_em_dias('olá', 14, 1) == Exception


print("Passou todos os testes!")
