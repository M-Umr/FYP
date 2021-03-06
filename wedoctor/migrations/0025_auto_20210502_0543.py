# Generated by Django 3.1.3 on 2021-05-02 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedoctor', '0024_patients_asspointment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients_asspointment',
            name='doctor_image',
            field=models.ImageField(blank=True, null=True, upload_to='appointment_doctor_profile'),
        ),
        migrations.AddField(
            model_name='patients_asspointment',
            name='patient_image',
            field=models.ImageField(blank=True, null=True, upload_to='appointment_patient_profile'),
        ),
    ]
