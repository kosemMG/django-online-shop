# Generated by Django 3.0.6 on 2020-05-13 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='product name')),
                ('img', models.ImageField(blank=True, upload_to='product_img')),
                ('color', models.CharField(max_length=31, verbose_name='product colour')),
                ('size', models.CharField(max_length=3, verbose_name='product size')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='product price')),
                ('quantity', models.SmallIntegerField(verbose_name='product amount')),
                ('shipping', models.CharField(max_length=31, verbose_name='product shipping')),
                ('link', models.CharField(max_length=31, verbose_name='product link')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ProductCategory')),
            ],
        ),
    ]
