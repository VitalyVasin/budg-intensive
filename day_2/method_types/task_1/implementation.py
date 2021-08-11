class Coffee:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __str__(self):
        return f'Coffee Class'

    @classmethod
    def get_cappuchino(cls):
        ingredients = ['coffee', 'milk', 'sugar']
        return cls(ingredients)

    @classmethod
    def get_latte(cls):
        ingredients = ['coffee', 'milk']
        return cls(ingredients)

    @classmethod
    def get_ice_coffee(cls):
        ingredients = ['coffee', 'milk', 'ice cream']
        return cls(ingredients)

if __name__ == '__main__':
    c = Coffee.get_latte()
    print(c)