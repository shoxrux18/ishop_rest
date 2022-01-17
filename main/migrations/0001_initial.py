# Generated by Django 4.0.1 on 2022-01-17 18:38

from django.db import migrations, models
import django.db.models.deletion
import ishop.helpers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=50)),
                ('name_en', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=ishop.helpers.UploadTo('category'))),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=50)),
                ('name_en', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=ishop.helpers.UploadTo('category'))),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.category')),
            ],
        ),
    ]
