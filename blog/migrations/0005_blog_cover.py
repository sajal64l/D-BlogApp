# Generated by Django 3.2.4 on 2021-06-08 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210607_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
