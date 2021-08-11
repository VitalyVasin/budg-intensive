class Tuple(tuple):
    """
    Создает неизменяемый объект, с упорядоченной структурой, методами count и index.
    При создание принимается последовательность объектов
    """
    def count(self, value):
        """
        Возвращает число раз появления value в объекте
        Args:
            value: Элемент число вхождения которого ищется в объекте
        """
        counter = 0
        for elements in Tuple:
            if elements == value:
                counter += 1
        return counter

    def index(self, value):
        """
        Возвращает индекс первого вхождения элемента в объекте
        Args:
            value: Элемент индекс которого ищется в объекте
        """
        try:
            index = 0
            for elements in Tuple:
                if elements == value:
                    return index
                index += 1

        except ValueError:
            print('No elements in Tuple')