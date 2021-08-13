class Multiplier:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return repr(self.value)
    # def __str__(self):
    #     return str(self.value)


class Hundred(Multiplier):
    """Множитель на 100"""
    def __init__(self, value):
        self.value = value*100

    def __repr__(self):
        return repr(self.value)

    def __add__(self, other):
        return Hundred((self.value + other.value)//100)

    def __sub__(self, other):
        return Hundred((self.value - other.value)//100)

    def __mul__(self, other):
        return Hundred((self.value * other.value)//100)

    def __truediv__(self, other):
        return Hundred((self.value / other.value)//100)

    def get_value(self):
        self.get_value = repr(self.value)
        print(self.get_value)
        return int(self.get_value)


class Thousand(Multiplier):
    """Множитель на 1 000"""
    def __init__(self, value):
        self.value = value*1000

    def __repr__(self):
        return repr(self.value)

    def __add__(self, other):
        return Thousand((self.value + other.value)//1000)

    def __sub__(self, other):
        return Thousand((self.value - other.value)//1000)

    def __mul__(self, other):
        return Thousand((self.value * other.value)//1000)

    def __truediv__(self, other):
        return Thousand((self.value / other.value)//1000)

    def get_value(self):
        self.get_value = repr(self.value)
        print(self.get_value)
        return int(self.get_value)


class Million(Multiplier):
    """Множитель на 1 000 000"""
    def __init__(self, value):
        self.value = value*1000000

    def __repr__(self):
        return repr(self.value)

    def __add__(self, other):
        return Million((self.value + other.value)//100000)

    def __sub__(self, other):
        return Million((self.value - other.value)//100000)

    def __mul__(self, other):
        return Million((self.value * other.value)//100000)

    def __truediv__(self, other):
        return Million((self.value / other.value)//100000)

    def get_value(self):
        self.get_value = repr(self.value)
        print(self.get_value)
        return int(self.get_value)

num = Hundred(10)
num2 = Hundred(2)
num.get_value()
num2.get_value()
num3 = num + num2
num3.get_value()
print(num3.get_value)



