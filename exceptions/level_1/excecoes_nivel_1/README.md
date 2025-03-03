# Python Exceptions Handling

Este repositório contém exemplos e desafios práticos sobre o tratamento de exceções em Python, demonstrando boas práticas para lidar com erros e situações inesperadas no código.

## 📋 Conteúdo

- Implementações de funções com tratamento de exceções
- Desafios de diferentes níveis de complexidade
- Exemplos práticos de uso de blocos `try/except`
- Demonstrações de como criar exceções personalizadas

## 🚀 Exemplo de Implementação

Abaixo está um exemplo de uma função que implementa tratamento de exceções para divisão segura:

```python
def divisao_segura(x: float, y: float):
    try:
        divisao = x / y
    except ZeroDivisionError:
        return 'Erro: Divisão por zero não permitida.'
    except TypeError:
        return 'Erro: Ambos os valores devem ser números.'
    except Exception as e:
        return f'Erro inesperado: {e}'
    return divisao
```

## 💡 Conceitos Abordados

### Principais Tipos de Exceções
- `ZeroDivisionError`: Ocorre quando tentamos dividir por zero
- `TypeError`: Ocorre quando uma operação é aplicada a um objeto de tipo inadequado
- `ValueError`: Ocorre quando uma função recebe um argumento com valor inadequado
- `FileNotFoundError`: Ocorre quando tentamos acessar um arquivo que não existe
- `IndexError`: Ocorre quando tentamos acessar um índice fora do intervalo em uma sequência

### Estruturas de Tratamento
- Blocos `try/except`: Capturam e tratam exceções
- Cláusula `else`: Executa código quando nenhuma exceção é levantada
- Cláusula `finally`: Executa código independentemente de ocorrer exceção ou não
- `raise`: Levanta exceções explicitamente

## 🎯 Desafios

O repositório contém desafios de diferentes níveis:

1. **Nível 1**: Tratamento básico de exceções comuns
2. **Nível 2**: Uso avançado de múltiplos blocos `except` e cláusulas `else`/`finally`
3. **Nível 3**: Criação e uso de exceções personalizadas

## 🛠️ Pré-requisitos

- Python 3.6 ou superior
- Conhecimentos básicos de programação em Python

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com:
- Novos exemplos de tratamento de exceções
- Desafios adicionais
- Correções ou melhorias na documentação
- Implementações alternativas

## 📝 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.