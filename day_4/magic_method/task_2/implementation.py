class MathClock:
    # hour = 0
    # minuts = 0
    def __init__(self, hour = 0, minuts = 0):
        self.hour = hour
        self.minuts = minuts

    def __repr__(self):
        return repr(self.hour+self.minuts)

    def __add__(self, other):
        return MathClock(self.minuts + other)

    def __sub__(self, other):
        return MathClock(self.minuts - other)

    def __mul__(self, other):
        return MathClock(self.hour + other)

    def __truediv__(self, other):
        return MathClock(self.hour - other)

    def get_time(self):
        print(self.hour, self.minuts)
        return self.hour, self.minuts

my_clock = MathClock()
# print(repr(my_clock))
my_clock * 5
my_clock.get_time()


