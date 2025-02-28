num1 = input('Digite um número inteiro: ')
num2 = input('Digite um número decimal: ')
num3 = input('Digite o outro número inteiro: ')

try:
    resultado1 = int(num1) + float(num2)
    soma_str = str(resultado1)
    
    resultado2 = int(num3) + 5
    num3_str = str(resultado2)
    
    print('Resultado da soma: ' + soma_str + ' e o número final é ' + num3_str)
except ValueError:
    print('Valor inválido! Digite o que se pede na pergunta.')