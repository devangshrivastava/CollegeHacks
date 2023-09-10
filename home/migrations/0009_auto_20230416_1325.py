# Generated by Django 3.2.17 on 2023-04-16 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuploadfile',
            name='batch',
            field=models.CharField(choices=[('2024', '2024'), ('2025', '2025'), ('2026', '2026')], max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='myuploadfile',
            name='course',
            field=models.CharField(choices=[('PRML', 'PRML'), ('Software Engineering', 'Software Engineering'), ('Mathematics-1', 'Mathematics-1'), ('Mathematics-2', 'Mathematics-2')], max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='myuploadfile',
            name='type',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='myuploadfile',
            name='f_name',
            field=models.CharField(max_length=250, null=True),
        ),
    ]