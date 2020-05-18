from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    phone = models.CharField(verbose_name='phone number', max_length=63)
    address = models.CharField(verbose_name='address', max_length=255)
    avatar = models.ImageField(upload_to='user_avatars', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.email})'
