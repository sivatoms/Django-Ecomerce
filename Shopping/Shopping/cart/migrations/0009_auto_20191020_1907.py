# Generated by Django 2.2.4 on 2019-10-20 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_auto_20191020_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_bucket',
            name='checked_out',
            field=models.BooleanField(default=False, verbose_name='checked_out'),
        ),
    ]
