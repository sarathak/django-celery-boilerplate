from datetime import datetime

import redis
from celery import shared_task
from django.conf import settings

from orders.models import Order


def get_number(date_key):
    r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
    return r.incr(date_key, )


@shared_task
def create_order(products, price):
    created = datetime.now()
    date_key = created.strftime('%Y%m%d')
    number = get_number(date_key)
    order_number = f'{date_key}-{number:05d}'
    Order.objects.create(order_number=order_number, products=products, price=price, created=created)
