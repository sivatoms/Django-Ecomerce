# Generated by Django 2.2.4 on 2019-10-26 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0017_auto_20191024_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='media/profile_images/'),
        ),
    ]