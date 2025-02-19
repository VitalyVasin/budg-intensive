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
    # оставлены части "сборки" для более удобной проверки
    # part1 = [int(str(num1)[0])+int(str(num1)[-1]) for num1 in list1 if len(str(num1)) > 1 and str(num1)[0] == str(num1)[len(str(num1))-1]]

    for num2 in list2:
        num2_str = str(num2)
        if len(num2_str) == 3 and num2 % 2 == 0:
            out2 = sqrt(num2)
            list2_out.append(out2)
    # оставлены части "сборки" для более удобной проверки
    # part2 = [sqrt(num2) for num2 in list2 if len(str(num2)) == 3 and num2 % 2 == 0]

    for num3 in list3:
        if num3 % 2 == 1 or num3 == 4:
            list3_out.append(num3)
    # оставлены части "сборки" для более удобной проверки
    # part3 =[num3 for num3 in list3 if num3 % 2 == 1 or num3 == 4]

    great_list = [int(a*b*c) for a in [int(str(num1)[0])+int(str(num1)[-1]) for num1 in list1 if len(str(num1)) > 1 and str(num1)[0] == str(num1)[len(str(num1))-1]] for b in [sqrt(num2) for num2 in list2 if len(str(num2)) == 3 and num2 % 2 == 0] for c in [num3 for num3 in list3 if num3 % 2 == 1 or num3 == 4]]


    return great_list