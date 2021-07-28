# Generated by Django 3.2.4 on 2021-07-28 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trequest', '0034_transportrequest_list_of_passengers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='driver',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Trequest.driver'),
        ),
        migrations.CreateModel(
            name='MaterialRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OldMaterial', models.CharField(max_length=200)),
                ('NewMaterial', models.CharField(max_length=200)),
                ('Amount', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('Reusable', 'reusable'), ('Usable', 'usable')], max_length=200, null=True)),
                ('RequestedBy', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='StoreManager', to=settings.AUTH_USER_MODEL)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Trequest.material')),
            ],
        ),
    ]
