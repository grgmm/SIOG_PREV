# Generated by Django 2.2.6 on 2020-01-01 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0011_auto_20200101_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='email',
        ),
    ]
