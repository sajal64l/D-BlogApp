# Generated by Django 3.2.4 on 2021-06-07 10:03

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210607_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
