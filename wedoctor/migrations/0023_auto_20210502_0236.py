# Generated by Django 3.1.3 on 2021-05-01 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedoctor', '0022_patients_asspointment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patients_asspointment',
            name='date',
        ),
        migrations.AlterField(
            model_name='patients_asspointment',
            name='booking_date',
            field=models.DateTimeField(default=''),
        ),
    ]
