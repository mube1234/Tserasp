# Generated by Django 3.2.5 on 2021-07-10 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trequest', '0033_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='transportrequest',
            name='list_of_passengers',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
    ]
