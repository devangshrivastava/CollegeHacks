# Generated by Django 3.2.17 on 2023-04-08 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20230408_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='date_created',
        ),
    ]