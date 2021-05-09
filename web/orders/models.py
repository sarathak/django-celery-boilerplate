from decimal import Decimal

from django.db import models


class Order(models.Model):
    order_number = models.CharField(max_length=20, )  # more than 1 billion order per day
    products = models.CharField(max_length=200, null=True, blank=True)  # just just for a sample
    price = models.DecimalField(default=Decimal('0.0'), decimal_places=2, max_digits=8)
    created = models.DateTimeField()

    def __str__(self):
        return self.order_number
