# Generated by Django 2.2.3 on 2019-08-23 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20190823_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimages',
            name='image',
            field=models.ImageField(upload_to='products_images/'),
        ),
    ]
