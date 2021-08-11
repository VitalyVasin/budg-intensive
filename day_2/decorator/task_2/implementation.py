from day_2.common import MyException

def check_value(func):
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """
    def wrapper(a):
        try:
            if not isinstance(a, int) or a < 0:
                raise MyException
            else:
                func(a)
        except MyException:
            raise MyException

        return func(a)

    return wrapper

