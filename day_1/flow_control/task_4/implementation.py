from datetime import (date)

"""Возвращает следующую дату для заданной

Args:
    some_date: определенная исходная дата

Returns: следующая дата
"""

def get_next_date(some_date):
    d, m, y = some_date.day, some_date.month, some_date.year
    if d == 28 and m == 2 and (y % 4 !=0):
        new_day = 1                            # условие для последнего дня февраля не високосного года
        new_month = m + 1
        new_year = y
    elif d == 29 and m == 2 and (y % 4 == 0):
        new_day = 1                            # условие для последнего дня февраля високосного года
        new_month = m + 1
        new_year = y
    elif d == 30 and (m == 4 or m == 6 or m == 9 or m == 11):
        new_day = 1                            # условие для последнего дня апреля, июня, сентября, ноября
        new_month = m + 1
        new_year = y
    elif d == 31 and (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10):
        new_day = 1                            # условие для последнего дня января, марта, мая, июля, августа, октября
        new_month = m + 1
        new_year = y
    elif d == 31 and m == 12:
        new_day = 1                             # условие для последнего дня декабря
        new_month = 1
        new_year = y + 1
    else:
        new_day = d + 1                         # условие для остальных случаев
        new_month = m
        new_year = y

    date_tomorrow = date(new_year, new_month, new_day)
    return date_tomorrow

