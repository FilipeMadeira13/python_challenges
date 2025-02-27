# Desafio: Variáveis e Tipos de Dados em Python

Um pequeno projeto que resolve um desafio de manipulação de variáveis e tipos de dados em Python, com ênfase em legibilidade do código.

---

## 🎯 Objetivo
Demonstrar o uso de:
- Declaração de variáveis (string, int, float, bool)
- Formatação de strings com f-strings
- Controle de casas decimais em números
- Exibição personalizada de valores booleanos

## 📋 Detalhes do Desafio
**Requisito Original:**  
Criar uma mensagem formatada que inclua:
- Nome (string)
- Idade (int)
- Altura com 2 casas decimais (float)
- Status de estudante (boolean em minúsculas)

## 🛠 Minha Solução
```python
nome = 'Filipe'
idade = 37
altura = 1.74
eh_estudante = True

print(f'Olá, meu nome é {nome}. Tenho {idade} anos, minha altura é {altura:.2f}m, e é {"verdade" if eh_estudante else "falso"} que sou estudante.')