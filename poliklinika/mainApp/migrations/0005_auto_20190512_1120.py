# Generated by Django 2.1.5 on 2019-05-12 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_auto_20190512_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='assistent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='analyse', to='mainApp.Assistent', verbose_name='Лаборант'),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='analyse', to='mainApp.Doctor', verbose_name='Врач'),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='out_patient_card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='analyse', to='mainApp.OutPatientCard', verbose_name='Амбулаторная карта'),
        ),
    ]
