# Desafio de Manipulação de Listas em Python 🐍

Este repositório contém a solução para um desafio de nível 1 sobre manipulação de listas em Python, com foco em operações básicas como adição, remoção e ordenação de elementos.

---

## 📋 Descrição do Desafio

O objetivo era criar uma função `manipula_lista()` que realiza uma série de operações em uma lista, seguindo etapas específicas:
1. Partir de uma lista vazia.
2. Adicionar elementos em ordem específica.
3. Remover um elemento específico.
4. Inserir elementos em posições definidas.
5. Reverter e ordenar a lista.

**Saída Esperada:** `[1, 2, 4, 5, 8]`

---

## 🚀 Solução

### Funcionalidades Implementadas
- Uso de métodos de lista: `append()`, `remove()`, `insert()`, `reverse()`, `sort()`.
- Lógica sequencial para garantir o resultado correto.
- Documentação clara da função.

### Como Funciona
A função executa as operações na seguinte ordem:
```python
1. Adiciona 5, 3, 8, 1 → [5, 3, 8, 1]
2. Remove 3 → [5, 8, 1]
3. Adiciona 4 → [5, 8, 1, 4]
4. Insere 2 no início → [2, 5, 8, 1, 4]
5. Inverte → [4, 1, 8, 5, 2]
6. Ordena → [1, 2, 4, 5, 8]