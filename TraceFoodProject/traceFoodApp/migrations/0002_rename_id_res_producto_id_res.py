# Generated by Django 4.0.6 on 2022-09-13 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traceFoodApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='id_Res',
            new_name='id_res',
        ),
    ]
