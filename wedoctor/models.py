from django.db import models
from django.forms import TimeInput
from phone_field import forms
from django import forms

from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime

# Create your models here.


class Patinet(models.Model):
    patient_id = models.AutoField
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, default="")
    birth_month = models.CharField(max_length=50, default="")
    birth_day = models.IntegerField(default=0)
    birth_year = models.IntegerField(max_length=4)
    sex = models.CharField(max_length=9)
    contact_no = PhoneNumberField()
    email = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    confirm_password = models.CharField(max_length=300)
    full_address = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    zip_cod = models.IntegerField(max_length=50)
    weight = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    image= models.ImageField(null=True,blank=True,upload_to="patient_profile")
    appointment_link = models.CharField(max_length=300,default="")


    def __str__(self):
        return self.first_name


class Doctor(models.Model):
    patient_id = models.AutoField
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, default="")
    birth_month = models.CharField(max_length=50, default="")
    birth_day = models.IntegerField(default=0)
    birth_year = models.IntegerField(max_length=4)
    sex = models.CharField(max_length=9)
    contact_no = PhoneNumberField()
    email = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    confirm_password = models.CharField(max_length=300)
    full_address = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    zip_cod = models.IntegerField(max_length=50)
    spc = models.CharField(max_length=600,default="")
    license = models.IntegerField(max_length=50)
    image = models.ImageField(null=True, blank=True, upload_to="doctor_profile")

    def __str__(self):
        return self.first_name


class Doctor_schedule(models.Model):
    appointment_id = models.AutoField
    doctor_email=models.CharField(max_length=300)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, default="")
    appointment_slot=models.CharField(max_length=1)
    monday=models.CharField(max_length=30,default="")
    tuesday=models.CharField(max_length=30,default="")
    wednesday=models.CharField(max_length=30,default="")
    thursday=models.CharField(max_length=30,default="")
    friday=models.CharField(max_length=30,default="")
    saturday=models.CharField(max_length=30,default="")
    sunday=models.CharField(max_length=30,default="")
    start_time=models.CharField(max_length=30,default="")
    end_time=models.CharField(max_length=30,default="")
    availability=models.CharField(max_length=30,default="")

    def __str__(self):
        return self.first_name

class Patients_asspointment(models.Model):

    patient_id=models.AutoField
    patient_email=models.CharField(max_length=30,default="")
    patient_first_name = models.CharField(max_length=30, default="")
    patient_last_name = models.CharField(max_length=30, default="")
    patient_city = models.CharField(max_length=50,default="")
    patient_province = models.CharField(max_length=50,default="")
    patient_contact_no = PhoneNumberField(default="")
    doctor_email=models.CharField(max_length=30,default="")
    appointment_status=models.CharField(max_length=30,default="")
    booking_date=models.DateTimeField(default="")
    appointment_day=models.CharField(max_length=30,default="")
    amount=models.CharField(max_length=30,default="")
    doctor_first_name=models.CharField(max_length=30,default="")
    doctor_last_name=models.CharField(max_length=30,default="")
    doctor_spec=models.CharField(max_length=30,default="")
    appointment_time=models.CharField(max_length=30,default="")
    date=models.CharField(max_length=30,default="")
    doctor_image = models.ImageField(null=True, blank=True, upload_to="appointment_doctor_profile")
    patient_image = models.ImageField(null=True, blank=True, upload_to="appointment_patient_profile")
    prescription_date = models.CharField(max_length=30, default="")
    appointment_link=models.CharField(max_length=100, default="")




class Prescription(models.Model):

    patient_id = models.AutoField
    patient_email = models.CharField(max_length=30, default="")
    patient_first_name = models.CharField(max_length=30, default="")
    patient_last_name = models.CharField(max_length=30, default="")
    patient_city = models.CharField(max_length=50, default="")
    patient_province = models.CharField(max_length=50, default="")
    patient_contact_no = PhoneNumberField(default="")
    doctor_email = models.CharField(max_length=30, default="")
    booking_date = models.DateTimeField(default="")
    appointment_day = models.CharField(max_length=30, default="")
    doctor_first_name = models.CharField(max_length=30, default="")
    doctor_last_name = models.CharField(max_length=30, default="")
    appointment_time = models.CharField(max_length=30, default="")
    date = models.CharField(max_length=30, default="")
    doctor_image = models.ImageField(null=True, blank=True, upload_to="pription")
    medicine= models.CharField(max_length=30, default="")
    time = models.CharField(max_length=60, default="")
    disease = models.CharField(max_length=30, default="")
    quantity = models.CharField(max_length=30, default="")
    days=models.CharField(max_length=30, default="")
    prescription_date = models.CharField(max_length=30, default="")
    instructions = models.CharField(max_length=2000, default="")




