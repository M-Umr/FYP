# Generated by Django 3.1.3 on 2020-12-09 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedoctor', '0004_auto_20201209_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specilization',
            field=models.CharField(default='', max_length=600),
        ),
    ]
