# Generated by Django 2.1.5 on 2019-05-12 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0014_auto_20190512_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reception',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
