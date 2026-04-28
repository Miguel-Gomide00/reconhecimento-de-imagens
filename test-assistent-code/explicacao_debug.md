# Explicação e correção de erros em `debug.py`

Este arquivo documenta os erros encontrados em `debug.py`, explica por que eles ocorrem e mostra como foram corrigidos.

## Erro 1: String de prompt sem aspas

Linha original:

```python
item1 = float(input(Preço do item 1? ))
```

- Problema: o texto do prompt não estava entre aspas.
- Efeito: causa `SyntaxError` antes mesmo do programa iniciar.
- Correção:

```python
item1 = float(input("Preço do item 1? "))
```

## Erro 2: Conversão de cupom de desconto não foi feita

Linha original:

```python
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
```

- Problema: `input()` retorna uma string.
- Efeito: usar `desconto_cupom / 100` gera `TypeError` porque string não pode ser dividida por número.
- Correção:

```python
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
```

## Erro 3: Falta de `f` em string formatada

Linha original:

```python
print(" Item 2:        R$ {total_item2:.2f}")
```

- Problema: a string não é um f-string.
- Efeito: o valor de `total_item2` não é interpolado e o texto `"{total_item2:.2f}"` é exibido literalmente.
- Correção:

```python
print(f" Item 2:        R$ {total_item2:.2f}")
```

## Erro 4: Indentação inválida no bloco `if`

Linha original:

```python
if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

- Problema: a linha dentro do `if` não estava indentada.
- Efeito: causa `IndentationError` e o bloco condicional não é válido.
- Correção:

```python
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

## Resultado final

O código agora funciona corretamente e exibe um recibo formatado com:

- nome do cliente
- valores totais dos itens
- subtotal
- imposto de 10%
- desconto, se aplicável
- valor total final

O arquivo `debug.py` corrigido está pronto para ser executado sem erros de sintaxe ou tipo.