# Generated by Django 3.2.5 on 2021-08-25 20:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trequest', '0073_auto_20210825_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='phone',
            field=models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format : 0987654321 or +251987654321 up to 15 digits allowed', regex='^(09|\\+2519)\\d{8}$')]),
        ),
    ]
