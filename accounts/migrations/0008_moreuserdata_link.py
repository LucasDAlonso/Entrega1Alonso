# Generated by Django 4.0.6 on 2022-08-01 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_moreuserdata_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='moreuserdata',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
