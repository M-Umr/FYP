# Generated by Django 3.1.3 on 2021-05-26 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedoctor', '0031_prescription_instructions'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients_asspointment',
            name='appointment_link',
            field=models.CharField(default='', max_length=100),
        ),
    ]
