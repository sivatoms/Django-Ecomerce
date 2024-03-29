# Generated by Django 2.2.4 on 2019-10-24 02:24

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0012_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, default=-6777, help_text='Contact phone number', max_length=31),
            preserve_default=False,
        ),
    ]
