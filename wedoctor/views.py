from django.http import HttpResponse
import os
from tkinter import *
import numpy as np
import pandas as pd
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponse, render, redirect
from django.contrib import messages
from .models import Doctor, Patinet,Doctor_schedule,Patients_asspointment,Prescription


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def predictdisease(request):
    return render(request, 'predict_disease.html')


def setappointments(request):
    return render(request, 'set_appointments.html')


def doctors(request):
    current_user = request.user
    doctor = Doctor.objects.filter(email=current_user)


    return render(request, 'doctors.html', {'doctor': doctor[0]})


def patientDashboard(request):
    current_user=request.user
    profile = Patinet.objects.filter(email=current_user)


    patient = Patients_asspointment.objects.filter(patient_email=current_user)



    return render(request, 'patient_dashboard.html',{'patient':patient,'profile':profile[0]})




def priscription_invoice_doctor(request):
    if request.method == "POST":
        patient_email = request.POST.get('patient_email', '')
        doctor_email = request.POST.get('doctor_email', '')
        date = request.POST.get('date', '')
        appointment_day = request.POST.get('appointment_day', '')
        appointment_time = request.POST.get('appointment_time', '')
        prescription = Prescription.objects.filter(patient_email=patient_email, doctor_email=doctor_email,
                                                   date=date, appointment_day=appointment_day,
                                                   appointment_time=appointment_time)


    return render(request, 'priscription_invoice_doctor.html',{'prescription':prescription[0]})


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')


def login(request):
    return render(request, 'login.html')


def signupForPatient(request):
    return render(request, 'signupforpatient.html')


def signupForDoctor(request):
    return render(request, 'signupfordoctor.html')


def patientProfile(request):
    return render(request, 'patientprofile.html')


def updateprofile(request):
    current_user = request.user
    patient = Patinet.objects.filter(email=current_user).first()

    return render(request, 'update_profile.html', {'patient': patient})


def updateDoctorProfile(request):
    current_user = request.user
    doctor = Doctor.objects.get(email=current_user)
    if request.method == "POST":
        image_file = request.FILES['profile_image']

        doctor.image = image_file
        doctor.save()

        doctor = Doctor.objects.filter(email=current_user).first()

        return render(request, 'update_profile_doctor.html', {'doctor': doctor})

    return render(request, 'update_profile_doctor.html', {'doctor': doctor})


def livecallDoctor(request):
    if request.method == "POST":
        current_user = request.user
        doctor = Doctor.objects.get(email=current_user)
        patient_mail = request.POST.get('email', '')
        patient_mail_url = request.POST.get('eemail', '')
        appointment_date = request.POST.get('id', '')
        appointment_day = request.POST.get('appointment_day', '')
        appointment_time = request.POST.get('appointment_time', '')
        doctor_email = request.POST.get('doctor_email', '')




        patient = Patients_asspointment.objects.filter(patient_email=patient_mail,date=appointment_date)
        if patient_mail and patient_mail_url:
            print(appointment_date)

            patient = Patients_asspointment.objects.get(patient_email=patient_mail,date=appointment_date,appointment_day=appointment_day,appointment_time=appointment_time,doctor_email=doctor_email)
            patient.appointment_link = patient_mail_url
            patient.save()

            patient = Patients_asspointment.objects.filter(patient_email=patient_mail, date=appointment_date)


        return render(request, 'livecall_doctor.html', {'patient_mail': patient_mail,'doctor':doctor,'patient':patient[0],'appointment_date':appointment_date,'appointment_day':appointment_day,'appointment_time':appointment_time,'doctor_email':doctor_email})


    return render(request, 'livecall_doctor.html')



def livecallPatient(request):
    patient_mail = request.user
    patient = Patinet.objects.get(email=patient_mail)
    patient_appoint_link = patient.appointment_link

    if request.method == "POST":
        patient_appoint_link = request.POST.get('appointment_link', '')




    return render(request, 'livecall_patient.html',{'patient_appoint_link':patient_appoint_link})


def prescription(request):
    if request.method == "POST":
        current_user = request.user
        doctor = Doctor.objects.get(email=current_user)
        patient_mail = request.POST.get('patient_email', '')
        doctor_mail = request.POST.get('doctor_malil', '')
        appointment_date = request.POST.get('date', '')

        patient =Patients_asspointment.objects.get(patient_email=patient_mail, date=appointment_date)
        patient.appointment_link = ""
        patient.save()

        patient = Patients_asspointment.objects.filter(patient_email=patient_mail, date=appointment_date)


        return render(request, 'prescription.html', {'patient': patient[0],'doctor':doctor})

    return render(request, 'prescription.html')

def my_patients_doctor(request):
    current_user = request.user
    doctor = Doctor.objects.filter(email=current_user)
    return render(request, 'my_patients_doctor.html',{'doctor':doctor[0]})

def appointment_requests_doctor(request):

    current_user = request.user
    patients = Patients_asspointment.objects.filter(doctor_email=current_user)

    doctor = Doctor.objects.filter(email=current_user)

    return render(request, 'appointment_requests_doctor.html',{'doctor':doctor[0],'patients':patients})



def prescribe_medicine_livecall(request):
    current_user = request.user
    patinet = Patients_asspointment.objects.filter(doctor_email=current_user)
    doctor = Doctor.objects.filter(email=current_user)


    return render(request, 'prescribe_medicine_livecall.html',{'patinet':patinet,'doctor':doctor[0]})



def map_doctor(request):
    current_user = request.user
    doctor = Doctor.objects.filter(email=current_user)
    return render(request, 'map_doctor.html',{'doctor':doctor[0]})


def map_admin(request):
    return render(request, 'map_admin.html')


def make_appointment(request):
    doctors = Doctor.objects.values()



    return render(request, 'make_appointment.html',{'doctors': doctors})


def book_appointment(request):


    if request.method == "POST":
        email = request.POST.get('email', '')
        doctor = Doctor.objects.filter(email=email)

    get_doctor_schedule = Doctor_schedule.objects.filter(doctor_email=email)

    all_secdule = []
    if len(get_doctor_schedule)>0:
        current_user = request.user
        patient = Patinet.objects.filter(email=current_user)

        monday_schedule = Doctor_schedule.objects.filter(doctor_email=email,monday='Monday')
        tuesday_schedule = Doctor_schedule.objects.filter(doctor_email=email, tuesday='Tuesday')
        wednesday_schedule = Doctor_schedule.objects.filter(doctor_email=email, wednesday='Wednesday')
        thursday_schedule = Doctor_schedule.objects.filter(doctor_email=email, thursday='Thursday')
        friday_schedule = Doctor_schedule.objects.filter(doctor_email=email, friday='Friday')
        saturday_schedule = Doctor_schedule.objects.filter(doctor_email=email, saturday='Saturday')
        sunday_schedule = Doctor_schedule.objects.filter(doctor_email=email, sunday='Sunday')
        all_secdule.append([monday_schedule,tuesday_schedule,wednesday_schedule,thursday_schedule,friday_schedule,saturday_schedule,sunday_schedule])

        return render(request, 'book_appointment.html',{'doctor_schedule':all_secdule,'monday_schedule':monday_schedule,'tuesday_schedule':tuesday_schedule,
                                                        'wednesday_schedule':wednesday_schedule,'thursday_schedule':thursday_schedule,
                                                        'friday_schedule':friday_schedule,'saturday_schedule':saturday_schedule,
                                                        'sunday_schedule':sunday_schedule,'get_doctor_schedule':get_doctor_schedule,'current_user':request.user,'doctor':doctor[0],'patient':patient[0]})
    else:
        return render(request, 'book_appointment.html', {'doctor_schedule': get_doctor_schedule,'doctor':doctor[0]})





def map_patient(request):
    return render(request, 'map_patient.html')

def getdata(request):





    return render(request, 'map_patient.html')


# def patient_profile_2(request):
#     return render(request, 'patient_profile_2.html')

def calendar(request):
    email=request.user
    current_user = request.user
    doctor = Doctor.objects.filter(email=current_user)
    get_doctor_schedule = Doctor_schedule.objects.filter(doctor_email=email)
    if len(get_doctor_schedule) > 0:


        monday_schedule1 = Doctor_schedule.objects.filter(doctor_email=email, monday='Monday',appointment_slot='1')
        monday_schedule2 = Doctor_schedule.objects.filter(doctor_email=email, monday='Monday',appointment_slot='2')
        monday_schedule3 = Doctor_schedule.objects.filter(doctor_email=email, monday='Monday', appointment_slot='3')
        tuesday_schedule1 = Doctor_schedule.objects.filter(doctor_email=email, tuesday='Tuesday',appointment_slot='1')
        tuesday_schedule2 = Doctor_schedule.objects.filter(doctor_email=email, tuesday='Tuesday', appointment_slot='2')
        tuesday_schedule3 = Doctor_schedule.objects.filter(doctor_email=email, tuesday='Tuesday', appointment_slot='3')
        wednesday_schedule1 = Doctor_schedule.objects.filter(doctor_email=email, wednesday='Wednesday',appointment_slot='1')
        wednesday_schedule2 = Doctor_schedule.objects.filter(doctor_email=email, wednesday='Wednesday',appointment_slot='2')
        wednesday_schedule3 = Doctor_schedule.objects.filter(doctor_email=email, wednesday='Wednesday',appointment_slot='3')
        thursday_schedule1 = Doctor_schedule.objects.filter(doctor_email=email, thursday='Thursday',appointment_slot='1')
        thursday_schedule2 = Doctor_schedule.objects.filter(doctor_email=email, thursday='Thursday',appointment_slot='2')
        thursday_schedule3 = Doctor_schedule.objects.filter(doctor_email=email, thursday='Thursday',appointment_slot='3')
        friday_schedule1 = Doctor_schedule.objects.filter(doctor_email=email, friday='Friday',appointment_slot='1')
        friday_schedule2 = Doctor_schedule.objects.filter(doctor_email=email, friday='Friday', appointment_slot='2')
        friday_schedule3 = Doctor_schedule.objects.filter(doctor_email=email, friday='Friday', appointment_slot='3')
        saturday_schedule1 = Doctor_schedule.objects.filter(doctor_email=email, saturday='Saturday',appointment_slot='1')
        saturday_schedule2 = Doctor_schedule.objects.filter(doctor_email=email, saturday='Saturday',appointment_slot='2')
        saturday_schedule3 = Doctor_schedule.objects.filter(doctor_email=email, saturday='Saturday',appointment_slot='3')
        sunday_schedule1 = Doctor_schedule.objects.filter(doctor_email=email, sunday='Sunday',appointment_slot='1')
        sunday_schedule2 = Doctor_schedule.objects.filter(doctor_email=email, sunday='Sunday', appointment_slot='2')
        sunday_schedule3 = Doctor_schedule.objects.filter(doctor_email=email, sunday='Sunday', appointment_slot='3')


        return render(request, 'calendar.html',{'monday_schedule1':monday_schedule1,'monday_schedule2':monday_schedule2,
                                                        'monday_schedule3':monday_schedule3,'tuesday_schedule1':tuesday_schedule1,
                                                        'tuesday_schedule2':tuesday_schedule2,'tuesday_schedule3':tuesday_schedule3,
                                                     'wednesday_schedule1':wednesday_schedule1,'wednesday_schedule2':wednesday_schedule2,
                                                'wednesday_schedule3':wednesday_schedule3, 'thursday_schedule1':thursday_schedule1,'thursday_schedule2':thursday_schedule2,
                                                'thursday_schedule3':thursday_schedule3,'friday_schedule1':friday_schedule1,'friday_schedule2':friday_schedule2,
                                                'friday_schedule3':friday_schedule3,'saturday_schedule1':saturday_schedule1,'saturday_schedule2':saturday_schedule2,
                                                'saturday_schedule3':saturday_schedule3,'sunday_schedule1':sunday_schedule1,'sunday_schedule2':sunday_schedule2,'sunday_schedule3':sunday_schedule3,'doctor':doctor[0]})
    else:
        return render(request, 'calendar.html',{'doctor':doctor[0]})

def adminprofile(request):
    return render(request, 'admin_profile.html')


def singnout(request):
    logout(request)
    messages.success(request, 'success full logout')
    return redirect('index')


