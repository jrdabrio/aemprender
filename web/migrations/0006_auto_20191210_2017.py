# Generated by Django 2.0.3 on 2019-12-10 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20191209_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='actividad_completada',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alumno',
            name='porcentaje_completado',
            field=models.IntegerField(default=0),
        ),
    ]