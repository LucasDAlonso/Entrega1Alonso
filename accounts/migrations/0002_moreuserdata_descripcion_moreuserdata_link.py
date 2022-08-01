# Generated by Django 4.0.6 on 2022-08-01 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moreuserdata',
            name='descripcion',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='moreuserdata',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
