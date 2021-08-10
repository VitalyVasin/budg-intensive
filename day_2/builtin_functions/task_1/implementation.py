from day_2.common import (
    MyException,
)

class Value:
    def __init__(self, argument):
        self.argument = argument

    def __add__(self, other):
        return other + self.argument

    def __sub__(self, other):
        return self.argument - other

    def __mul__(self, other):
        return self.argument * other

    def __truediv__(self, other):
        try:
            div = self.argument / other

        except ZeroDivisionError:
            raise MyException
        return div


