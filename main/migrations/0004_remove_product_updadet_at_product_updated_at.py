# Generated by Django 4.0.1 on 2022-01-24 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_added_at_product_available_product_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='updadet_at',
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
