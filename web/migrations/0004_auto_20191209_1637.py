# Generated by Django 2.0.3 on 2019-12-09 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_actividadtres_respuestastres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividadcinco',
            name='plantilla',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='respuestascinco',
            name='valor',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
