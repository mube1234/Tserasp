# Generated by Django 3.2.5 on 2021-08-11 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trequest', '0055_transportrequest_is_expired'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transportrequest',
            name='is_expired',
        ),
        migrations.AlterField(
            model_name='transportrequest',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=200),
        ),
        migrations.AlterField(
            model_name='transportrequest',
            name='status2',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=200),
        ),
        migrations.AlterField(
            model_name='transportrequest',
            name='status3',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=200),
        ),
    ]