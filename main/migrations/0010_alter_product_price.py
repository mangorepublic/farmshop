# Generated by Django 4.0.1 on 2022-05-25 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_product_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
