# Generated by Django 4.0.1 on 2022-05-24 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_product_added_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
