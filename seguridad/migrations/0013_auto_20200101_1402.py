# Generated by Django 2.2.6 on 2020-01-01 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0012_remove_usuario_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='id_gdp',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='id_planta',
        ),
        migrations.AddField(
            model_name='estandar',
            name='id_procesos',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proceso',
            name='id_estandar',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='planta',
            name='id_estandar',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id_planta',
            field=models.CharField(max_length=30),
        ),
    ]
