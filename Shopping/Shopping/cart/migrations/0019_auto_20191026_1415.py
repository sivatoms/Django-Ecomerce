# Generated by Django 2.2.4 on 2019-10-26 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0018_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='cart/profile_images/'),
        ),
    ]