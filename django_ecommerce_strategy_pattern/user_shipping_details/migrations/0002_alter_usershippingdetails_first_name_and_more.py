# Generated by Django 5.1.3 on 2024-11-24 17:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_shipping_details', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usershippingdetails',
            name='first_name',
            field=models.CharField(blank=True, validators=[django.core.validators.RegexValidator(message='Please make sure your First Name contains only letters', regex='^[A-Za-z]$'), django.core.validators.MinLengthValidator(2, message='First name must be at least 2 characters long'), django.core.validators.MaxLengthValidator(255, message=('First name cannot be longer than 255 characters',))]),
        ),
        migrations.AlterField(
            model_name='usershippingdetails',
            name='last_name',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='This field requires $2-$255 letters', regex='^[A-Za-z]{2,255}$')]),
        ),
        migrations.AlterField(
            model_name='usershippingdetails',
            name='phone_number',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='This field requires $7-$15 digits', regex='^[0-9]{7,15}$')]),
        ),
    ]
