# Generated by Django 2.1.5 on 2019-05-12 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0009_auto_20190512_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workgrafic',
            name='friday_start',
            field=models.CharField(choices=[('0', 'Выходной'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], max_length=20, null=True, verbose_name='Пятница начало работы'),
        ),
        migrations.AlterField(
            model_name='workgrafic',
            name='friday_stop',
            field=models.CharField(choices=[('0', 'Выходной'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], max_length=20, null=True, verbose_name='Пятница конец работы'),
        ),
        migrations.AlterField(
            model_name='workgrafic',
            name='monday_start',
            field=models.CharField(choices=[('0', 'Выходной'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], max_length=20, null=True, verbose_name='Понедельник начало работы'),
        ),
        migrations.AlterField(
            model_name='workgrafic',
            name='monday_stop',
            field=models.CharField(choices=[('0', 'Выходной'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], max_length=20, null=True, verbose_name='Понедельник конец работы'),
        ),
        migrations.AlterField(
            model_name='workgrafic',
            name='saturday_start',
            field=models.CharField(choices=[('0', 'Выходной'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], max_length=20, null=True, verbose_name='Суббота начало работы'),
        ),
        migrations.AlterField(
            model_name='workgrafic',
            name='saturday_stop',
            field=models.CharField(choices=[('0', 'Выходной'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], max_length=20, null=True, verbose_name='Суббота конец работы'),
        ),
        migrations.AlterField(
            model_name='workgrafic',
            name='thursday_start',
            field=models.CharField(choices=[('0', 'Выходной'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], max_length=20, null=True, verbose_name='Четверг начало работы'),
        ),
        migrations.AlterField(
            model_name='workgrafic',
            name='thursday_stop',
            field=models.CharField(choices=[('0', 'Выходной'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], max_length=20, null=True, verbose_name='Четверг конец работы'),
        ),
        migrations.AlterField(
            model_name='workgrafic',
            name='tuesday_start',
            field=models.CharField(choices=[('0', 'Выходной'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], max_length=20, null=True, verbose_name='Вторник начало работы'),
        ),
        migrations.AlterField(
            model_name='workgrafic',
            name='tuesday_stop',
            field=models.CharField(choices=[('0', 'Выходной'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], max_length=20, null=True, verbose_name='Вторник конец работы'),
        ),
        migrations.AlterField(
            model_name='workgrafic',
            name='wednesday_start',
            field=models.CharField(choices=[('0', 'Выходной'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], max_length=20, null=True, verbose_name='Среда начало работы'),
        ),
        migrations.AlterField(
            model_name='workgrafic',
            name='wednesday_stop',
            field=models.CharField(choices=[('0', 'Выходной'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], max_length=20, null=True, verbose_name='Среда конец работы'),
        ),
    ]
