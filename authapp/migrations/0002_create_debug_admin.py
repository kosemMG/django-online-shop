from django.conf import settings
from django.db import migrations


def forwards_func(apps, schema_editor):
    if settings.DEBUG:
        # Only in DEBUG mode!
        try:
            from authapp.models import ShopUser

            ShopUser.objects.create_superuser("admin", "root@test.com", "admin")
        except:
            print("Cannot create super user for debug")


def reverse_func(apps, schema_editor):
    if settings.DEBUG:
        # Only in DEBUG mode!
        try:
            from authapp.models import ShopUser

            ShopUser.objects.all().delete()
        except:
            print("Cannot delete super user for debug")


class Migration(migrations.Migration):
    dependencies = [("authapp", "0001_initial")]

    operations = [migrations.RunPython(forwards_func, reverse_func)]
