objeto = input('Digite um nome de um objeto: ')
try:
    quantidade = int(input('Digite a quantidade desse objeto: '))
    preco_unitario = float(input('Digite o preço de uma unidade desse objeto: '))
    desconto = input('Desconto aplicável? [True/False] ').lower() == 'true'
    
    preco_total = quantidade * preco_unitario
    
    print(f'Objeto: {objeto}')
    print(f'Quantidade: {quantidade}')
    print(f'Preço Unitário: R${preco_unitario:.2f}')
    print(f'Desconto aplicável: {'Sim' if desconto else 'Não'}')
    print(f'Preço total: R${preco_total:.2f}')
except ValueError:
    print('Entrada inválida! Digite apenas números inteiros para a quantidade e números para o preço')