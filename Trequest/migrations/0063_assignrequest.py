# Generated by Django 3.2.5 on 2021-08-23 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trequest', '0062_transportrequest_is_expired'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_to', models.EmailField(max_length=254)),
                ('date_to', models.DateField()),
                ('time_to', models.TimeField()),
                ('driver_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trequest.driver')),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
