# Generated by Django 3.2.17 on 2023-04-17 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_myuploadfile_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuploadfile',
            name='type',
        ),
    ]
