def counter(func):
    """
    Обертка для подсчёта количества вызовов обернутой функции.

    Returns:
        int - количество вызовов функции.
    """

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1

        return count

    count = 0
    return wrapper
