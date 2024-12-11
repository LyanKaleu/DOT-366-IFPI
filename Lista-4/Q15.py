def pesquisar_habitantes(salarios, filhos):
    if type(salarios) != list or type(filhos) != list:
        return Exception
    
    if len(salarios) != len(filhos) or len(salarios) == 0:
        return Exception
    
    for salario in salarios:
        if (type(salario) != int and type(salario) != float) or salario < 0:
            return Exception
        
    for num_filhos in filhos:
        if type(num_filhos) != int or num_filhos < 0:
            return Exception
    

    total_pessoas = len(salarios)
    soma_salarios = sum(salarios)
    soma_filhos = sum(filhos)
    maior_salario = max(salarios)
    quantidade_salario_ate_350 = sum(1 for salario in salarios if salario <= 350)

    media_salario = soma_salarios / total_pessoas
    media_filhos = soma_filhos / total_pessoas
    percentual_salario_ate_350 = (quantidade_salario_ate_350 / total_pessoas) * 100

    return round(media_salario, 2), round(media_filhos, 2), round(maior_salario, 2), round(percentual_salario_ate_350, 2)


# Valores válidos
assert pesquisar_habitantes([1000, 350, 250], [2, 3, 1]) == (533.33, 2.0, 1000, 66.67) 
assert pesquisar_habitantes([400, 400, 400], [1, 1, 1]) == (400, 1.0, 400, 0.0)
assert pesquisar_habitantes([100, 200, 300], [0, 2, 3]) == (200, 1.67, 300, 100.0)

# Valores inválidos
assert pesquisar_habitantes([], []) == Exception
assert pesquisar_habitantes([1000, 350], [2]) == Exception
assert pesquisar_habitantes([1000, -350], [2, 3]) == Exception
assert pesquisar_habitantes([1000, 350], [2, -3]) == Exception
assert pesquisar_habitantes([1000, '350'], [2, 3]) == Exception
assert pesquisar_habitantes(1000, [2, 3]) == Exception
assert pesquisar_habitantes([1000, 350], 3) == Exception

print("Passou todos os testes!")
