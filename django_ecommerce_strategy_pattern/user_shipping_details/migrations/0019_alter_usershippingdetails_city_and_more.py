# Generated by Django 5.1.3 on 2024-11-25 12:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_shipping_details', '0018_alter_usershippingdetails_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usershippingdetails',
            name='city',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='Please make sure the City name contains only letters', regex='^[A-Za-z]+$'), django.core.validators.MinLengthValidator(limit_value=2, message='City name must be at least 2 characters long'), django.core.validators.MaxLengthValidator(limit_value=255, message=('City name cannot be longer than 255 characters',))]),
        ),
        migrations.AlterField(
            model_name='usershippingdetails',
            name='country',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='Please make sure the Country name contains only letters', regex='^[A-Za-z]+$'), django.core.validators.MinLengthValidator(limit_value=2, message='Country name must be at least 2 characters long'), django.core.validators.MaxLengthValidator(limit_value=255, message=('Country name cannot be longer than 255 characters',))]),
        ),
        migrations.AlterField(
            model_name='usershippingdetails',
            name='first_name',
            field=models.CharField(error_messages={'blank': 'Please enter your First Name'}, validators=[django.core.validators.RegexValidator(message='Please make sure your First Name contains only letters', regex='^[A-Za-z]+$'), django.core.validators.MinLengthValidator(limit_value=2, message='First Name must be at least 2 characters long'), django.core.validators.MaxLengthValidator(limit_value=255, message=('First Name cannot be longer than 255 characters',))]),
        ),
        migrations.AlterField(
            model_name='usershippingdetails',
            name='last_name',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='Please make sure your Last Name contains only letters', regex='^[A-Za-z]+$'), django.core.validators.MinLengthValidator(limit_value=2, message='Last Name must be at least 2 characters long'), django.core.validators.MaxLengthValidator(limit_value=255, message=('Last Name cannot be longer than 255 characters',))]),
        ),
        migrations.AlterField(
            model_name='usershippingdetails',
            name='phone_number',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='Please make sure your Phone Number contains only digits', regex='^[0-9]+$'), django.core.validators.MinLengthValidator(limit_value=7, message='Phone Number must be at least 7 digits long'), django.core.validators.MaxLengthValidator(limit_value=15, message='Phone Number cannot be longer than 15 digits')]),
        ),
    ]