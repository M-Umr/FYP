# Generated by Django 3.1.3 on 2020-12-09 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedoctor', '0003_auto_20201209_1936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='specilizatio',
            new_name='specilization',
        ),
    ]