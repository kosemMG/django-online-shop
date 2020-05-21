from django.conf import settings
from django.db import models

from mainapp.models import Product


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(verbose_name="amount", default=0)
    add_datetime = models.DateTimeField(verbose_name="adding time", auto_now_add=True)
