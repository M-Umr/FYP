# Generated by Django 3.1.3 on 2021-05-01 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedoctor', '0023_auto_20210502_0236'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients_asspointment',
            name='date',
            field=models.CharField(default='', max_length=30),
        ),
    ]