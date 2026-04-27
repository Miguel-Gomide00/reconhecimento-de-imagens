# Explicação da Função `is_prime`

Esta função verifica se um número `n` é primo. Um número primo é maior que 1 e só divisível por 1 e por ele mesmo.

```python
def is_prime(n):
    if n <= 1:
        return False
```

- `def is_prime(n):`: Define a função que recebe um parâmetro `n` (o número a verificar).
- `if n <= 1:`: Verifica se `n` é menor ou igual a 1. Números menores ou iguais a 1 não são primos.
- `return False`: Retorna `False` se a condição for verdadeira.

```python
    if n == 2:
        return True
```

- `if n == 2:`: 2 é o único número par primo.
- `return True`: Retorna `True` para 2.

```python
    if n % 2 == 0:
        return False
```

- `if n % 2 == 0:`: Verifica se `n` é par (divisível por 2). Números pares maiores que 2 não são primos.
- `return False`: Retorna `False` se for par.

```python
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
```

- `for i in range(3, int(n**0.5) + 1, 2):`: Loop de 3 até a raiz quadrada de `n` (aproximadamente), pulando números pares (passo 2).
- `if n % i == 0:`: Verifica se `n` é divisível por `i`.
- `return False`: Se divisível, não é primo.

```python
    return True
```

- `return True`: Se passou por todas as verificações, `n` é primo.






