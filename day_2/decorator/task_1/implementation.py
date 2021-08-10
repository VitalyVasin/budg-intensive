from day_2.common import factorial
import time


def time_execution(func):
    """
    Обертка, печатающая время выполнения функции.
    """
    def subfunc(*args, **kwargs):
        start_time = time.time()
        result_func = func(*args, **kwargs)
        end_time = time.time()
        result_time = round(end_time - start_time, 4)
        print('Функция работала ', result_time, ' секунд')
        return result_func
    return subfunc


@time_execution
def factorial(number):
    """
    Возвращает факториал переданного числа
    Args:
        number: число, для которого надо посчитать факториал

    Returns:
        product - int - факториал от number
    """
    product = 1
    for element in range(1, number+1):
        product *= element

    return product

test = factorial(11111)