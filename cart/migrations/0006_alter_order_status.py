# Generated by Django 4.0.1 on 2022-02-09 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Yangi'), (1, 'Qabul qilingan'), (2, 'Qaytarilgan'), (3, "Yo'lda"), (4, 'Yetkazib berilgan'), (5, 'Yopilgan')], default=0),
        ),
    ]
