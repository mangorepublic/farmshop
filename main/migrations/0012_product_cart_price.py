# Generated by Django 4.0.1 on 2022-05-25 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cart_price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
