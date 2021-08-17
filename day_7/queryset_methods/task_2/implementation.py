def get_top_customer_in_period(begin, end):
    """Возвращает покупателя, который сделал наибольшее количество заказов за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает имя покупателя и количество его заказов за указанный период
    """
    name = ProductCount.objects.filter(date_formation__gt = begin, bdate_formation__lt = end).order_by(-'name').first()
    order_count = ProductCount.objects.filter(date_formation__gt = begin, bdate_formation__lt = end, name = name).count()
    return name, order_count
