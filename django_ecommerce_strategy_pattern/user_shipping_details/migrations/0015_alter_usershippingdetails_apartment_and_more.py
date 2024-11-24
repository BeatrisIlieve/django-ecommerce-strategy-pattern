# Generated by Django 5.1.3 on 2024-11-25 11:42

import django.core.validators
import django_ecommerce_strategy_pattern.user_shipping_details.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_shipping_details', '0014_alter_usershippingdetails_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usershippingdetails',
            name='apartment',
            field=models.CharField(validators=[django.core.validators.MaxLengthValidator(10, message=('Apartment cannot be longer than 10 characters',))]),
        ),
        migrations.AlterField(
            model_name='usershippingdetails',
            name='city',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='Please make sure the City name contains only letters', regex='^[A-Za-z]$'), django.core.validators.MinLengthValidator(limit_value=2, message='City name must be at least 2 characters long'), django.core.validators.MaxLengthValidator(limit_value=255, message=('City name cannot be longer than 255 characters',))]),
        ),
        migrations.AlterField(
            model_name='usershippingdetails',
            name='country',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='Please make sure the Country name contains only letters', regex='^[A-Za-z]$'), django.core.validators.MinLengthValidator(limit_value=2, message='Country name must be at least 2 characters long'), django.core.validators.MaxLengthValidator(limit_value=255, message=('Country name cannot be longer than 255 characters',))]),
        ),
        migrations.AlterField(
            model_name='usershippingdetails',
            name='first_name',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='Please make sure your First Name contains only letters', regex='^[A-Za-z]$'), django_ecommerce_strategy_pattern.user_shipping_details.validators.Validator(error_message='please enter your first name', length_limit=0, method=django_ecommerce_strategy_pattern.user_shipping_details.validators.ValidationMethod['ZERO_LENGTH']), django_ecommerce_strategy_pattern.user_shipping_details.validators.Validator(error_message='First Name must be at least 2 characters long', length_limit=2, method=django_ecommerce_strategy_pattern.user_shipping_details.validators.ValidationMethod['MIN_LENGTH']), django.core.validators.MaxLengthValidator(limit_value=255, message=('First Name cannot be longer than 255 characters',))]),
        ),
        migrations.AlterField(
            model_name='usershippingdetails',
            name='last_name',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='Please make sure your Last Name contains only letters', regex='^[A-Za-z]$'), django.core.validators.MinLengthValidator(limit_value=2, message='Last Name must be at least 2 characters long'), django.core.validators.MaxLengthValidator(limit_value=255, message=('Last Name cannot be longer than 255 characters',))]),
        ),
        migrations.AlterField(
            model_name='usershippingdetails',
            name='phone_number',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='Please make sure your Phone Number contains only digits', regex='^[0-9]$'), django.core.validators.MinLengthValidator(limit_value=7, message='Phone Number must be at least 7 digits long'), django.core.validators.MaxLengthValidator(limit_value=15, message='Phone Number cannot be longer than 15 digits')]),
        ),
        migrations.AlterField(
            model_name='usershippingdetails',
            name='postal_code',
            field=models.CharField(validators=[django.core.validators.MinLengthValidator(4, message='Postal Code must be at least 4 characters long'), django.core.validators.MaxLengthValidator(15, message=('Postal Code cannot be longer than 15 characters',))]),
        ),
        migrations.AlterField(
            model_name='usershippingdetails',
            name='street',
            field=models.CharField(validators=[django.core.validators.MinLengthValidator(limit_value=8, message='Street must be at least 8 characters long'), django.core.validators.MaxLengthValidator(limit_value=255, message=('Street cannot be longer than 255 characters',))]),
        ),
    ]
