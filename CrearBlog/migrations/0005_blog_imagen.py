# Generated by Django 4.0.6 on 2022-08-01 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrearBlog', '0004_blog_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='blos'),
        ),
    ]
