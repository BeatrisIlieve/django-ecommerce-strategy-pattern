# Generated by Django 5.1.3 on 2024-11-24 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_credential_details', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercredentialdetails',
            name='email',
            field=models.EmailField(error_messages={'invalid': 'Please enter a valid email address'}, max_length=254, unique=True),
        ),
    ]