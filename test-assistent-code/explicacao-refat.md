# Explicação da Refatoração em `refatoracao.py`

O arquivo `refatoracao.py` contém uma função para verificar se um número é primo, com boas práticas de legibilidade e nomenclatura.

```python
"""Funções utilitárias refatoradas para verificação de números primos."""
```

- Esta docstring descreve o propósito geral do arquivo.
- Ela ajuda outros desenvolvedores a entenderem rapidamente que o módulo contém utilitários relacionados a números primos.

```python
from math import isqrt
```

- Importa a função `isqrt` do módulo `math`.
- `isqrt` calcula a raiz quadrada inteira de um número com precisão e eficiência.

```python
def is_prime(number: int) -> bool:
```

- Define a função `is_prime` que recebe um argumento chamado `number`.
- A anotação `: int` indica que `number` deve ser um inteiro.
- `-> bool` indica que a função retorna um valor booleano (`True` ou `False`).

```python
    """Retorna True se o número for primo, caso contrário False."""
```

- Esta docstring interna descreve o comportamento da função.
- Ela explica que o retorno será `True` apenas quando o número for primo.

```python
    if number <= 1:
        return False
```

- Verifica se o número é menor ou igual a 1.
- Números 1, 0 e negativos não são primos, então retorna `False` imediatamente.

```python
    if number == 2:
        return True
```

- Verifica se o número é 2.
- O número 2 é o menor e único número par que é primo.
- Nesse caso, retorna `True`.

```python
    if number % 2 == 0:
        return False
```

- Verifica se o número é par e maior que 2.
- Se for divisível por 2, não é primo, então retorna `False`.

```python
    max_divisor = isqrt(number)
```

- Calcula a maior possível raiz quadrada inteira de `number`.
- Esse valor é suficiente para checar divisores até a raiz quadrada, evitando iterações extras.

```python
    for divisor in range(3, max_divisor + 1, 2):
```

- Inicia um loop que começa em 3 e vai até `max_divisor`, inclusive.
- O passo `2` faz o loop verificar apenas números ímpares.
- Números pares já foram eliminados, então não há necessidade de testá-los novamente.

```python
        if number % divisor == 0:
            return False
```

- Para cada divisor ímpar, verifica se `number` é divisível por ele.
- Se encontrar um divisor, o número não é primo e retorna `False` imediatamente.

```python
    return True
```

- Se nenhum divisor válido for encontrado até `max_divisor`, o número é primo.
- Retorna `True` como resultado final.

```python
if __name__ == "__main__":
```

- Verifica se o arquivo está sendo executado diretamente.
- Esse bloco não será executado se o módulo for importado por outro script.

```python
    exemplos = [2, 3, 4, 17, 18, 19, 20]
```

- Define uma lista de exemplos de números para testar a função.
- Facilita a demonstração do comportamento sem precisar interagir com o usuário.

```python
    resultados = {numero: is_prime(numero) for numero in exemplos}
```

- Cria um dicionário onde cada número é a chave e o valor é o resultado de `is_prime(numero)`.
- Usa compreensão de dicionário para deixar o código mais conciso e legível.

```python
    for numero, primo in resultados.items():
```

- Itera sobre os pares `chave:valor` do dicionário `resultados`.
- `numero` recebe o número testado e `primo` recebe o booleano retornado.

```python
        status = "primo" if primo else "não primo"
```

- Usa expressão condicional para transformar o resultado booleano em texto legível.
- `status` será `"primo"` se `primo` for `True`, caso contrário `"não primo"`.

```python
        print(f"{numero} é {status}.")
```

- Exibe no console o resultado de cada verificação.
- A mensagem fica no formato `número é primo.` ou `número é não primo.`.
