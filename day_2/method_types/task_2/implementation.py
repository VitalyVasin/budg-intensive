class ClassFather:
    try:
        def get_name(self, name):
            self.name = name

        def register(self):
            pass
    except MyException:
        raise MyException




class User1(ClassFather):
    _name = 'Chip'


class User2(ClassFather):
    _name = 'Dale'

