# Generated by Django 3.1.3 on 2021-05-26 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedoctor', '0032_patients_asspointment_appointment_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients_asspointment',
            name='doctor_spec',
            field=models.CharField(default='', max_length=30),
        ),
    ]