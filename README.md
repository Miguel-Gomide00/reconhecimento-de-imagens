# Reconhecimento de Imagens — Código de Exemplo

Este repositório contém uma coleção de scripts Python de exemplo dentro da pasta `test-assistent-code`, com foco em:

- depuração e correção de código (`debug.py`)
- verificação de números primos (`num_primos.py`)
- refatoração de funções e boas práticas em Python (`refatoracao.py`)
- documentação explicativa dos problemas e das soluções aplicadas

> Nota: apesar do nome do repositório, a pasta atual contém exemplos de lógica e refatoração em Python, não um projeto de reconhecimento de imagens.

## Estrutura do Projeto

```
reconhecimento-de-imagens/
├── README.md
└── test-assistent-code/
    ├── debug.py
    ├── num_primos.py
    ├── refatoracao.py
    ├── explicacao_debug.md
    ├── explicacao-num-prim.md
    └── explicacao-refat.md
```

## Scripts Principais

### `test-assistent-code/debug.py`

Um script interativo que:

- solicita o nome do cliente
- recebe quantidade e preço de três itens
- calcula subtotal, imposto fixo de 10% e desconto opcional
- imprime um recibo formatado

### `test-assistent-code/num_primos.py`

Contém a função `is_prime(n)` para verificar se um número inteiro é primo.

- retorna `False` para números menores ou iguais a 1
- trata `2` como primo
- descarta pares maiores que 2
- testa divisores ímpares até a raiz quadrada de `n`

### `test-assistent-code/refatoracao.py`

Uma versão refatorada da verificação de número primo:

- usa tipagem com `int` e `bool`
- usa `math.isqrt` para limitar o intervalo de divisores
- inclui um bloco `if __name__ == "__main__"` com exemplos de execução

## Documentação e Explicações

Os arquivos Markdown contêm explicações detalhadas sobre cada caso:

- `test-assistent-code/explicacao_debug.md`: análise e correção dos erros em `debug.py`
- `test-assistent-code/explicacao-num-prim.md`: explicação linha a linha da função `is_prime`
- `test-assistent-code/explicacao-refat.md`: explicação das melhorias em `refatoracao.py`

## Como Executar

Use Python 3 para rodar os scripts. A partir da raiz do repositório:

```bash
python test-assistent-code/debug.py
python test-assistent-code/num_primos.py
python test-assistent-code/refatoracao.py
```

### Exemplo de uso

Para testar se um número é primo diretamente no interpretador Python:

```python
from test_assistent_code.num_primos import is_prime
print(is_prime(17))
```

> Observação: o arquivo `num_primos.py` atual não é um pacote, então o exemplo acima funciona se o diretório `test-assistent-code` estiver configurado como módulo ou se você estiver executando a partir da raiz com ajustes de import.

## Requisitos

- Python 3.8+

## Recomendações

- Use ambientes virtuais (`venv`) para evitar conflitos de dependências
- Leia os arquivos `explicacao_*.md` para entender as correções e os motivos das mudanças
- Considere refatorar o código de `debug.py` em funções para melhorar a reutilização e os testes
