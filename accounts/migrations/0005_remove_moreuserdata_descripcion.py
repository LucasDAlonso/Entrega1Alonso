# Generated by Django 4.0.6 on 2022-08-01 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_moreuserdata_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moreuserdata',
            name='descripcion',
        ),
    ]