def calcular_estatisticas(numeros: list) -> dict:
    if not numeros:
        return None
    
    return {
        'soma': sum(numeros),
        'media': sum(numeros) / len(numeros),
        'maximo': max(numeros),
        'minimo': min(numeros)
    }

try:    
    numeros = [5, 2, 9, 1, 5, 6]
    resultado = calcular_estatisticas(numeros)
    print(resultado)
    print(calcular_estatisticas([]))
    print(calcular_estatisticas([7]))
except ZeroDivisionError:
    print('A média não pode ser dividida por zero')