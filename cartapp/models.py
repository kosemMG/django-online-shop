from django.conf import settings
from django.db import models

from mainapp.models import Product


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(verbose_name="amount", default=0)
    add_datetime = models.DateTimeField(verbose_name="adding time", auto_now_add=True)

    @property
    def product_cost(self):
        return self.product.price * self.amount

    @property
    def total_quantity(self):
        items = Cart.objects.filter(user=self.user)
        return sum(list(map(lambda x: x.amount, items)))

    @property
    def total_cost(self):
        items = Cart.objects.filter(user=self.user)
        return sum(list(map(lambda x: x.product_cost, items)))
