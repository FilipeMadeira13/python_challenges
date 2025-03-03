from string import ascii_letters

palavra = input('Digite uma palavra: ').strip()

try:
    for letra in palavra:
        if letra not in ascii_letters:
            raise TypeError
    
except TypeError:
    print('Erro: A palavra deve conter apenas letras')
else:
    for i, _ in enumerate(palavra, 1):
        print(palavra[:i])

    tamanho_palavra = len(palavra)

    while tamanho_palavra > 1:
        print(palavra[:tamanho_palavra - 1])
        tamanho_palavra -= 1