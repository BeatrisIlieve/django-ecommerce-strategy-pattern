# Generated by Django 5.1.3 on 2024-11-25 14:48

import django.core.validators
import django_ecommerce_strategy_pattern.user_payment_details.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_payment_details', '0002_alter_userpaymentdetails_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpaymentdetails',
            name='card_holder',
            field=models.CharField(error_messages={'blank': 'Please enter your First Name'}, validators=[django.core.validators.RegexValidator(message="Card Holder must be in the format 'John Doe'", regex='^[A-Z][a-z]+ [A-Z][a-z]+$'), django.core.validators.MinLengthValidator(limit_value=5, message='Card Holder name must be at least 5 characters long'), django.core.validators.MaxLengthValidator(limit_value=36, message=('Card Holder name cannot be longer than 36 characters',))]),
        ),
        migrations.AlterField(
            model_name='userpaymentdetails',
            name='card_number',
            field=models.CharField(error_messages={'blank': 'Please enter a valid Card Number'}, validators=[django.core.validators.RegexValidator(message='Please make sure your Card Number contains only digits', regex='^\\d+$'), django.core.validators.MinLengthValidator(limit_value='Card Number must be exactly 16 digits long', message='Card Number must be exactly 16 digits long'), django.core.validators.MaxLengthValidator(limit_value='Card Number must be exactly 16 digits long', message='Card Number must be exactly 16 digits long')]),
        ),
        migrations.AlterField(
            model_name='userpaymentdetails',
            name='cvv_code',
            field=models.CharField(error_messages={'blank': 'Please enter a CVV Code'}, validators=[django.core.validators.RegexValidator(message='Please make sure the CVV Code contains only digits', regex='^\\d+$'), django.core.validators.MinLengthValidator(limit_value=3, message='CVV Code must be exactly 3 digits long'), django.core.validators.MaxLengthValidator(limit_value=3, message='CVV Code must be exactly 3 digits long')]),
        ),
        migrations.AlterField(
            model_name='userpaymentdetails',
            name='expiry_date',
            field=models.DateField(null=True, validators=[django_ecommerce_strategy_pattern.user_payment_details.validators.validate_card_expiry_date]),
        ),
    ]