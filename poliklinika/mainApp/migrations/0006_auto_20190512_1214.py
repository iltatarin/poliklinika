# Generated by Django 2.1.5 on 2019-05-12 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_auto_20190512_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='medicina',
        ),
        migrations.AddField(
            model_name='doctor',
            name='photo',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Medicina',
        ),
    ]
