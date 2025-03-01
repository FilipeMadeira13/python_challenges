def manipula_lista():
    """Função para realizar operações em uma lista vazia."""
    lista = []
    # Adicionando elementos
    lista.append(5)
    lista.append(3)
    lista.append(8)
    lista.append(1)
    # Removendo o número 3
    lista.remove(3)
    # Adicionando o 4 no final da lista
    lista.append(4)
    # Inserindo o número 2 no início da lista
    lista.insert(0, 2)
    # Invertendo a ordem da lista
    lista.reverse()
    # Retornando a lista ordenada
    lista.sort()
    return lista
    
print(manipula_lista())