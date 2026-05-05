def is_prime(n):
    """Verifica se um número inteiro é primo.

    Args:
        n (int): Número inteiro a ser testado.

    Returns:
        bool: True se o número for primo, False caso contrário.

    Examples:
        >>> is_prime(7)
        True
        >>> is_prime(10)
        False
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True