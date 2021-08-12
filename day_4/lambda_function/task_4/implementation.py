class Product:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return repr(self.value)

a = Product(12)
b = Product(7)
c = Product(10)
my_list_product = [a, b, c]


res_list_product = []
res_list_product = list(filter(lambda number: number.value > 10, my_list_product))
