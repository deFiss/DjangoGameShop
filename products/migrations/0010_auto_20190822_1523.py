# Generated by Django 2.2.3 on 2019-08-22 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20190822_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimages',
            name='image',
            field=models.ImageField(upload_to='products_images/'),
        ),
    ]
