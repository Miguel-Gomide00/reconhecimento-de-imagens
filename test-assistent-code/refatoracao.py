"""Funções utilitárias refatoradas para verificação de números primos."""

from math import isqrt


def is_prime(number: int) -> bool:
    """Retorna True se o número for primo, caso contrário False."""
    if number <= 1:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    max_divisor = isqrt(number)
    for divisor in range(3, max_divisor + 1, 2):
        if number % divisor == 0:
            return False

    return True


if __name__ == "__main__":
    exemplos = [2, 3, 4, 17, 18, 19, 20]
    resultados = {numero: is_prime(numero) for numero in exemplos}
    for numero, primo in resultados.items():
        status = "primo" if primo else "não primo"
        print(f"{numero} é {status}.")
