from math import sqrt

list1 = [12, 2, 17, 44, 131]
list2 = [127, 69, 144, 0, 1024]
list3 = [8, 6, 5, 4, 7]

list1_out = []
list2_out = []
list3_out = []

def great_comprehension(list1, list2, list3):
    """
    Возвращает список с перемноженными элементами списков list1, list2 и list3 согласно условию
    """
    for num1 in list1:
        num1_str = str(num1)
        if len(num1_str) > 1 and num1_str[0] == num1_str[len(num1_str)-1]:
            out1 = int(num1_str[0])+int(num1_str[len(num1_str)-1])
            list1_out.append(out1)

    for num2 in list2:
        num2_str = str(num2)
        if len(num2_str) == 3 and num2 % 2 == 0:
            out2 = sqrt(num2)
            list2_out.append(out2)

    for num3 in list3:
        if num3 % 2 == 1 or num3 == 4:
            list3_out.append(num3)

    great_list = [list1_out[i]*list2_out[i]*list3_out[i] for i in range(min([len(list1_out), len(list2_out), len(list3_out)]))]
    # print('Great list is ', great_list)

great_comprehension(list1, list2, list3)
"""
Вам нужно написать comprehension который будет перемножать три значения из списков при некоторых условиях:
1. Если первая и последняя **ЦИФРА** для _ЧИСЛА_ из первого списка равны между собой, то вы берете сумму этих **ЦИФР** 
для дальнейшего умножения. Учитывайте что _ЧИСЛО_ не должно быть одноразрядным.
2. Если число из второго списка имеет 3 разряда и является четным, то вы берете квадратный корень от этого числа для 
дальнейшего умножения. (Функция sqrt из модуля math)
3. Если число из третьего списка НЕ четное или равно 4, то вы берете это число

Внутри итогового списка должны быть только int'овые значения
"""
