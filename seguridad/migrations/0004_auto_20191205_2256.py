# Generated by Django 2.2.6 on 2019-12-06 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0003_auto_20191205_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=12)),
                ('apellido', models.CharField(max_length=12)),
            ],
        ),
        migrations.DeleteModel(
            name='Usuariox',
        ),
    ]
