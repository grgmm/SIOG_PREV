# Generated by Django 2.2.6 on 2019-12-06 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0005_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='aor',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
