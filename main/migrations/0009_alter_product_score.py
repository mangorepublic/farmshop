# Generated by Django 4.0.1 on 2022-05-24 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_customusers_earning_alter_product_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='score',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
