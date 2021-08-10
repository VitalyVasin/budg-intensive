from datetime import (date)

"""Возвращает следующую дату для заданной

Args:
    some_date: определенная исходная дата

Returns: следующая дата
"""

def get_next_date(some_date):
    d, m, y = some_date.day, some_date.month, some_date.year
    SMALL_MONTH = (4, 6, 9, 11)
    BIG_MONTH = (1, 3, 5, 7, 8, 10)
    FEBRUARY = (2,)
    DECEMBER = (12,)
    # условие для последнего дня февраля не високосного года
    if d == 28 and (m in FEBRUARY) and (y % 4 !=0):
        new_day = 1
        new_month = m + 1
        new_year = y
    # условие для последнего дня февраля високосного года
    elif d == 29 and (m in FEBRUARY) and (y % 4 == 0):
        new_day = 1
        new_month = m + 1
        new_year = y
    # условие для последнего дня апреля, июня, сентября, ноября
    elif d == 30 and (m in SMALL_MONTH):
        new_day = 1
        new_month = m + 1
        new_year = y
    # условие для последнего дня января, марта, мая, июля, августа, октября
    elif d == 31 and (m in BIG_MONTH):
        new_day = 1
        new_month = m + 1
        new_year = y
    # условие для последнего дня декабря
    elif d == 31 and (m in DECEMBER):
        new_day = 1
        new_month = 1
        new_year = y + 1
    # условие для остальных случаев
    else:
        new_day = d + 1
        new_month = m
        new_year = y

    date_tomorrow = date(new_year, new_month, new_day)
    return date_tomorrow

