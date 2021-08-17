def get_top_product_by_total_count_in_period(begin, end):
    """Возвращает товар, купленный в наибольшем объеме за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает наименование товара и объем
    """
    Product = ProductCount.objects.filter(date_formation__gt = begin, bdate_formation__lt = end).order_by(-'name').first
    ValueProduct = ProductCount.objects.filter(date_formation__gt = begin, bdate_formation__lt = end).order_by(-'value').first
    return Product, ValueProduct
