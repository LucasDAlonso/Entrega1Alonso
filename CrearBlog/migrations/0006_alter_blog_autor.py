# Generated by Django 4.0.6 on 2022-08-01 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrearBlog', '0005_blog_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='autor',
            field=models.CharField(max_length=30),
        ),
    ]
