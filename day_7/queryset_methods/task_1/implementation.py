from django.db import models
from django.db.models import Manager


def get_order_count_by_customer(name):
    """Возвращает количества заказов по имени покупателя

    Args:
        name: имя покупателя

    Returns: число заказов (не может быть отрицательным, но может быть нулевым)
    """
    return Customer.objects.order_by('name')
