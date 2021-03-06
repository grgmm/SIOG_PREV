# Generated by Django 2.2.6 on 2020-01-01 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0010_auto_20191207_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estandar',
            name='id_procesos',
        ),
        migrations.RemoveField(
            model_name='proceso',
            name='id_estandar',
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(blank=True, max_length=70, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='id_gdp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguridad.Gdp'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='id_planta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguridad.Planta'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='planta',
            name='id_estandar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguridad.Estandar'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id_planta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguridad.Planta'),
        ),
    ]
