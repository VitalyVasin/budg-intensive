from day_2.common import MyException

def check_value(func):
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """
    def sub_func(a):
        try:
            if (type(a) != int) or (a == None) or a < 0:
                raise MyException
            else:
                func(a)
        except MyException:
            raise MyException

        return func(a)

    return sub_func

