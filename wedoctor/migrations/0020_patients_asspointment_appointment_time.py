# Generated by Django 3.1.3 on 2021-04-27 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedoctor', '0019_auto_20210427_0517'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients_asspointment',
            name='appointment_time',
            field=models.CharField(default='', max_length=30),
        ),
    ]
