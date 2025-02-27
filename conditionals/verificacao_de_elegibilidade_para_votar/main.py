try:
    idade = int(input('Digite sua idade: '))
    
    if idade < 0:
        print('Idade inválida. Por favor, insira um número positivo.')
    elif idade >= 18:
        print(f'Você pode votar! {"Este é o seu primeiro ano de votação." if idade == 18 else ""}')
    else:
        print(f'Você não pode votar. Volte em {18 - idade} anos!')
except ValueError:
    print('Entrada inválida. Digite apenas números inteiros.')