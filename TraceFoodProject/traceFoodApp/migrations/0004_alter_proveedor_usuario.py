# Generated by Django 4.0.6 on 2022-11-13 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traceFoodApp', '0003_rename_departameno_proveedor_departamento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='usuario',
            field=models.CharField(default=models.EmailField(max_length=254), max_length=20),
        ),
    ]
