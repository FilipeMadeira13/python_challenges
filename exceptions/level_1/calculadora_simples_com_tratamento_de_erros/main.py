class OperacaoInvalida(Exception):
    pass

try:
    numero_1 = float(input('Digite o primeiro número: '))
    numero_2 = float(input('Digite o segundo número: '))
    operador = input('Escolha a operação (+, -, *, /, %): ').strip()
    
    if operador not in ['+', '-', '*', '/', '%']:
        raise OperacaoInvalida('Operação inválida. Escolha apenas as operações citadas.')
    
    if operador == '+':
        resultado = numero_1 + numero_2
    elif operador == '-':
        resultado = numero_1 - numero_2
    elif operador == '*':
        resultado = numero_1 * numero_2
    elif operador == '/':
        resultado = numero_1 / numero_2
    elif operador == '%':
        resultado = numero_1 % numero_2
except ValueError:
    print('Erro: Digite apenas números.')
except ZeroDivisionError:
    print('Erro: números não podem ser divididos por zero.')
except OperacaoInvalida as e:
    print(f'Erro: {e}')
else:
    print(resultado)
finally:
    print('Fim da operação')