# Generated by Django 5.1.3 on 2024-11-25 14:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_shipping_details', '0020_alter_usershippingdetails_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usershippingdetails',
            name='first_name',
            field=models.CharField(error_messages={'blank': 'Please enter your First Name'}, validators=[django.core.validators.RegexValidator(message='Please make sure your First Name contains only letters', regex='^[A-Za-z]+$'), django.core.validators.MinLengthValidator(limit_value=2, message='First Name must be at least 2 characters long'), django.core.validators.MaxLengthValidator(limit_value=255, message=('First Name cannot be longer than 255 characters',))]),
        ),
    ]