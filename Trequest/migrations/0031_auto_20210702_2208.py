# Generated by Django 3.2.4 on 2021-07-02 19:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Trequest', '0030_auto_20210702_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='date_registered',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
    ]
