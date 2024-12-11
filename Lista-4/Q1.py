PI = 3.14

def volume_circulo(raio):
    if type(raio) == str or raio <= 0:
        return Exception
    
    return round(4/3 * PI * raio ** 3, 2)


# Valores válidos (inteiros e reais)
print(volume_circulo(3))
assert volume_circulo(3) == 113.04
assert volume_circulo(4.5) == 381.51
assert volume_circulo(10) == 4186.67

# Valores inválidos
assert volume_circulo(0) == Exception
assert volume_circulo(-4) == Exception
assert volume_circulo('palavra') == Exception
 

print("Passou todos os testes!")
