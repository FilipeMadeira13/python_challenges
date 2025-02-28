# De uma nota para a minha solução

try:
    n = int(input('Digite um número inteiro positivo: '))
    
    # Verifica se o número é positivo
    if n < 1:
        raise ValueError
    
    resultado = 0
    
    for i in range(1, n + 1):
        resultado += i
        
    print(f'A soma dos números de 1 até {n} é: {resultado}')
    
except ValueError:
    print('Entrada inválida! Digite apenas números inteiros positivos.')