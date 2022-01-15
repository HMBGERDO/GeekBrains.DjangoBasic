from django.conf import settings
from django.db import models
from django import template

from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="basket")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="количество", default=0)
    add_datetime = models.DateTimeField(verbose_name="время добавления", auto_now_add=True)

    @staticmethod
    def get_products_amount(user):
        amount = 0
        for product in Basket.objects.filter(user=user):
            amount += product.quantity
        return amount

    @staticmethod
    def get_total_price(user):
        total = 0
        for product in Basket.objects.filter(user=user):
            total += product.amount * product.product.price
        return total
