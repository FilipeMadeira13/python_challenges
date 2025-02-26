# Desafio de Fibonacci Modificado

Este projeto implementa uma variação interessante da sequência de Fibonacci clássica, com regras especiais aplicadas aos termos gerados.

## Descrição do Problema

A sequência de Fibonacci modificada segue estas regras:

1. Começa como a sequência tradicional (0, 1, 1, 2, 3, 5, 8, 13, 21, 34...)
2. Para cada número gerado:
   - Se for múltiplo de 3, substitua-o pelo seu dobro
   - Se for múltiplo de 5, substitua-o pela sua metade (arredondada para baixo)
   - Se for múltiplo de ambos, aplique as regras conforme a implementação escolhida

## Solução Implementada

```python
def sequencia_fibonacci_modificada(n):
    # Inicialização dos primeiros termos
    if n <= 0:
        return 0
    
    if n == 1:
        return 0
    
    # Usamos um loop for para gerar a sequência básica
    sequencia = [0, 1]
    for i in range(2, n):
        sequencia.append(sequencia[i-1] + sequencia[i-2])
    
    # Usamos um loop while para aplicar as modificações
    i = 0
    while i < len(sequencia):
        # Aplicamos as regras de modificação
        if sequencia[i] % 3 == 0 and sequencia[i] % 5 == 0:
            # Aplicamos ambas as regras: primeiro dobrar, depois dividir
            sequencia[i] = (sequencia[i] * 2) // 2
        elif sequencia[i] % 3 == 0:
            sequencia[i] = sequencia[i] * 2
        elif sequencia[i] % 5 == 0:
            sequencia[i] = sequencia[i] // 2
        i += 1
    
    # Retornamos a soma dos termos
    return sum(sequencia)
```

## Explicação da Solução

Esta implementação utiliza dois tipos diferentes de loops:
1. Um loop `for` para gerar a sequência de Fibonacci básica
2. Um loop `while` para aplicar as regras de modificação a cada termo

Para números que são múltiplos tanto de 3 quanto de 5, a solução aplica ambas as operações sequencialmente (dobra e depois divide por 2), o que efetivamente não altera o valor original.

## Como Usar

```python
# Gerar e modificar os primeiros 10 termos da sequência
resultado = sequencia_fibonacci_modificada(10)
print(f"A soma dos 10 primeiros termos modificados é: {resultado}")

# Para ver a sequência completa (não apenas a soma), modifique a função para retornar a lista
def ver_sequencia_completa(n):
    # Implementação da função conforme acima, mas retornando a lista em vez da soma
    ...
    return sequencia  # Retorna a lista completa em vez de sum(sequencia)
```

## Exemplos

- Sequência original: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
- Sequência modificada: 0, 1, 1, 2, 6, 2, 8, 13, 42, 34...
  - 3 → 6 (múltiplo de 3, então dobra)
  - 5 → 2 (múltiplo de 5, então divide por 2)
  - 21 → 42 (múltiplo de 3, então dobra)

## Considerações de Desempenho

Para valores grandes de `n`, esta implementação pode enfrentar limitações de desempenho devido à natureza recursiva da sequência de Fibonacci. Uma abordagem alternativa usando programação dinâmica ou fórmulas matemáticas diretas poderia ser mais eficiente para casos de uso com valores elevados de `n`.

## Desafios Adicionais

1. Modificar a implementação para usar diferentes regras de precedência nos números que são múltiplos tanto de 3 quanto de 5
2. Implementar uma versão otimizada para lidar com valores grandes de `n`
3. Visualizar graficamente a diferença entre a sequência original e a modificada