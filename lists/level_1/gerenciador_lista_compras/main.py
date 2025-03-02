# Inicialização da lista de compras
lista_compras = []

# Função para adicionar item à lista
def adicionar_item(item: str):
    if item in lista_compras:
        return f'{item.capitalize()} já está na lista de compras.'
        
    lista_compras.append(item)
    return f'{item.capitalize()} adicionado com sucesso.'

# Função para remover item da lista
def remover_item(item: str):
    if item not in lista_compras:
        return f'{item.capitalize()} não encontrado na lista de compras.'
    
    lista_compras.remove(item)
    return f'{item.capitalize()} removido com sucesso.'

# Função para exibir a lista completa
def exibir_lista():
    if not lista_compras:
        print('A lista está vazia.')
        return
    
    print('---LISTA DE COMPRAS---')
    for item in lista_compras:
        print(f'- {item.capitalize()}')

# Função para verificar se um item está na lista
def verificar_item(item: str):
    if item in lista_compras:
        return True
    return False

# Interface do usuário
def menu():
    print("\n===== GERENCIADOR DE LISTA DE COMPRAS =====")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Exibir lista")
    print("4. Verificar item")
    print("5. Sair")
    
    opcao = input("\nEscolha uma opção (1-5): ")
    
    if opcao == '1':
        item = input('Adicione um item a lista de compras: ').lower().strip()
        print(adicionar_item(item))
    elif opcao == '2':
        item = input('Digite um item para remover da lista de compras: ').lower().strip()
        print(remover_item(item))
    elif opcao == '3':
        exibir_lista()
    elif opcao == '4':
        item = input('Digite um item para verificar se está na lista de compras: ').lower().strip()
        na_lista = verificar_item(item)
        print(f'{item.capitalize()}{" não" if not na_lista else ""} está na lista de compras.')
    elif opcao == '5':
        return True
    else:
        print('Por favor, digite uma opção válida de 1 a 5.')

# Execução do programa
if __name__ == "__main__":
    print("Bem-vindo ao Gerenciador de Lista de Compras!")
    
    while True:
        sair = menu()
        if sair:
            print('Programa Encerrado.')
            break