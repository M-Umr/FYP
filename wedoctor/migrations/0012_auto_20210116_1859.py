# Generated by Django 3.1.3 on 2021-01-16 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedoctor', '0011_auto_20210116_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patinet',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='patient_profile/'),
        ),
    ]
