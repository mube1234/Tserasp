# Generated by Django 3.2.5 on 2021-08-01 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trequest', '0039_profile_bio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transportrequest',
            options={'ordering': ['-id']},
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_viewed', models.BooleanField(default=False)),
                ('request_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trequest.transportrequest')),
                ('sender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]