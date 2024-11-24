# Generated by Django 5.1.3 on 2024-11-24 17:09

import django_ecommerce_strategy_pattern.user_shipping_details.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_shipping_details', '0002_alter_usershippingdetails_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usershippingdetails',
            name='first_name',
            field=models.CharField(validators=[django_ecommerce_strategy_pattern.user_shipping_details.validators.Validator(error_message='First name must be at least 2 characters long', length_limit=0, method=django_ecommerce_strategy_pattern.user_shipping_details.validators.ValidationMethod['ZERO_LENGTH']), django_ecommerce_strategy_pattern.user_shipping_details.validators.Validator(error_message='First name must be at least 2 characters long', length_limit=2, method=django_ecommerce_strategy_pattern.user_shipping_details.validators.ValidationMethod['MIN_LENGTH']), django_ecommerce_strategy_pattern.user_shipping_details.validators.Validator(error_message=('First name cannot be longer than 255 characters',), length_limit=255, method=django_ecommerce_strategy_pattern.user_shipping_details.validators.ValidationMethod['MAX_LENGTH'])]),
        ),
    ]
