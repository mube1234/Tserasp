# Generated by Django 3.2.4 on 2021-07-04 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trequest', '0031_auto_20210702_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver_name', to='Trequest.driver'),
        ),
    ]
