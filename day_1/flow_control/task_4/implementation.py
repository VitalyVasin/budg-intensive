from datetime import (date, timedelta)

def get_next_date(some_date):
    """Возвращает следующую дату для заданной

    Args:
        some_date: определенная исходная дата

    Returns: следующая дата
    """
    date_tomorrow = some_date + timedelta(days=1)
    print(date_tomorrow)

    return date_tomorrow
