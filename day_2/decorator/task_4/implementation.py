from day_2.common import MyException, specific_func

def decorator_maker(times, delay):
    """
    Обертка, которая повторяет вызов функции times раз с паузой delay секунд
    Args:
        times: количество повторений
        delay: задержка (с)

    Returns:
        валидное значение (при вызове bool() -> True)
    """

    def wrapper(func):
        try:
            wrapper.count += 1
            func
            if func:
                print('true')
            else:
                if times > 0:
                    times -= 1
                    delay(delay * 1000)
                    wrapper(func)
                else:
                    raise MyException
        except AssertionError:
            raise MyException

        return func

    wrapper.count = 0
    return wrapper


