# Generated by Django 2.2.6 on 2020-01-12 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0018_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
