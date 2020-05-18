from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='product name', max_length=100)
    img = models.ImageField(upload_to='product_img', blank=True)
    color = models.CharField(verbose_name='product colour', max_length=31)
    size = models.CharField(verbose_name='product size', max_length=3)
    price = models.DecimalField(verbose_name='product price', max_digits=6, decimal_places=2)
    quantity = models.SmallIntegerField(verbose_name='product amount')
    shipping = models.CharField(verbose_name='product shipping', max_length=31)
    link = models.CharField(verbose_name='product link', max_length=31)

    def __str__(self):
        return f'{self.name} ({self.category.name})'
