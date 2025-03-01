# Calculadora de Estatísticas Básicas em Python 📊

Uma função simples em Python para calcular estatísticas básicas (soma, média, máximo e mínimo) de uma lista de números. Ideal para aprender o uso de funções e funções integradas do Python!

## Funcionalidades ⚙️

- Calcula a **soma**, **média**, **valor máximo** e **valor mínimo** de uma lista de números.
- Retorna os resultados em um dicionário formatado.
- Trata listas vazias retornando `None`.
- Suporta listas com um único elemento.

## Como Usar 🚀

### Pré-requisitos
- Python 3.x instalado.

### Instalação
1. Clone o repositório ou copie o código da função abaixo:

```python
def calcular_estatisticas(numeros: list) -> dict:
    if not numeros:
        return None
    
    return {
        'soma': sum(numeros),
        'media': sum(numeros) / len(numeros),
        'maximo': max(numeros),
        'minimo': min(numeros)
    }