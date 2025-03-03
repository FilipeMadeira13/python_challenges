# De uma nota para a minha solução

def divisao_segura(x: float, y: float):
    try:
        divisao = x / y
    except ZeroDivisionError:
        return'Erro: Divisão por zero não permitida.'
    except TypeError:
        return 'Erro: Ambos os valores devem ser números.'
    except Exception as e:
        return f'Erro inesperado: {e}'
    return divisao

print(divisao_segura(10, 2))
print(divisao_segura(10, 0))
print(divisao_segura("10", 2))