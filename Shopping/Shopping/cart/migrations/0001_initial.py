# Generated by Django 2.2.4 on 2019-10-18 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=200)),
                ('product_price', models.IntegerField()),
                ('product_image', models.ImageField(upload_to=None)),
            ],
        ),
    ]
