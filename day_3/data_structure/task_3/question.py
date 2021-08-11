"""
Посмотрите сколько памяти занимают следующие объекты.
Сколько будет занимать памяти список с двумя элементами после добавления в него
еще одно элемента с помощью append? Почему?
"""
import sys

first_tuple = (1, 2)
second_tuple = (1, 2, 3)
first_list = [1, 2]
second_list = [1, 2, 3]

print('first_tuple занимает: ', sys.getsizeof(first_tuple), 'байт')
print('second_tuple занимает: ', sys.getsizeof(second_tuple), 'байт')
print('first_list занимает: ', sys.getsizeof(first_list), 'байт')
print('second_list занимает: ', sys.getsizeof(second_list), 'байт')

first_list.append(3)
print('first_list с тремя элементами стал занимать: ', sys.getsizeof(first_list), 'байт')

"""
first_tuple занимает:  56 байт
second_tuple занимает:  64 байт
first_list занимает:  72 байт
second_list занимает:  80 байт
first_list с тремя элементами стал занимать:  104 байт
Список first_list, с двумя элементами, после добавления в него третьего элемента стал занимать в памяти 104 байта.
Это происходит из-за того что списки занимают больше на 1/3, из-за реализации алгоритма добавления новых элементов.
"""
