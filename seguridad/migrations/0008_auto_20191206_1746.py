# Generated by Django 2.2.6 on 2019-12-06 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0007_auto_20191206_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aor',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]