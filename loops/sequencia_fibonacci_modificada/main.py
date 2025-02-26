def sequencia_fibonacci_modificada(n):
    # Inicialização dos primeiros termos
    if n <= 0:
        return 0
    
    if n == 1:
        return 0
    
    # Loop for para gerar a sequência básica
    sequencia = [0, 1]
    for i in range(2, n):
        sequencia.append(sequencia[i-1] + sequencia[i-2])
    
    # Loop while para aplicar as modificações
    i = 0
    while i < len(sequencia):
        # Aplicamos as regras de modificação
        # Nota: podemos ter números que são múltiplos tanto de 3 quanto de 5
        if sequencia[i] % 3 == 0 and sequencia[i] % 5 == 0:
            # Decidimos aplicar ambas as regras: primeiro dobrar, depois dividir
            sequencia[i] = (sequencia[i] * 2) // 2
        elif sequencia[i] % 3 == 0:
            sequencia[i] = sequencia[i] * 2
        elif sequencia[i] % 5 == 0:
            sequencia[i] = sequencia[i] // 2
        i += 1
    
    # Retornamos a soma conforme solicitado
    return sum(sequencia)