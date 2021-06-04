"""wedoctor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views, database

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

                  # Basic Home Page
                  path('admin/', admin.site.urls),

                  path('', views.index, name="index"),
                  path('index/', views.index, name="index"),
                  path('about/', views.about, name="about"),
                  path('services/', views.services, name="services"),
                  path('doctors/', views.doctors, name="doctors"),
                  path('blog/', views.blog, name="blog"),
                  path('contact/', views.contact, name="contact"),
                  path('login/', views.login, name="login"),
                  path('singnin/', database.person.signin, name="user_signin"),
                  path('singnout/', views.singnout, name="user_singnout"),

                  # Doctors
                  path('setappointments/', views.setappointments, name="setappointments"),
                  path('my_patients_doctor/', views.my_patients_doctor, name="my_patients_doctor"),
                  path('priscription_invoice_doctor/', views.priscription_invoice_doctor, name="priscription_invoice_doctor"),
                  path('appointment_requests_doctor/', views.appointment_requests_doctor,
                       name="appointment_requests_doctor"),
                  path('livecall_doctor/', views.livecallDoctor, name="livecall_doctor"),
                  path('patient_medical_history/', database.doctor.view_patient_history, name="patient_medical_history"),
                  path('signupfordoctor/', views.signupForDoctor, name="signupfordoctor"),

                  path('prescribe_medicine_livecall/', views.prescribe_medicine_livecall,
                       name="prescribe_medicine_livecall"),
                  path('update_doctor_profile/', views.updateDoctorProfile, name="update_doctor_profile"),
                  path('calendar', views.calendar, name="calendar"),
                  path('mapdoctor', views.map_doctor, name="mapdoctor"),
                  path('makeappointment', views.make_appointment, name="makeappointment"),
                  path('bookappointment/', views.book_appointment, name="bookappointment"),

                  path('signupfordoctors/', database.doctor.signupfordoctors, name="signupfordoctors"),
                  ##############################
                  path('doctor_schdule/', database.doctor.set_appointments, name="update_schedule"),
                  path('prescription/', views.prescription, name="prescription"),
                  path('signup/', database.patient.signup, name="patientsignup"),
                  path('accept_appointment/', database.doctor.accept_appointment, name="accept_appointment"),
                  path('cancel_appointment/', database.doctor.cancel_appointment, name="cancel_appointment"),
                  path('prescribemedicine/', database.doctor.prescribemedicine, name="prescribemedicine"),



                  # Patients
                  path('signupforpatient/', views.signupForPatient, name="signupforpatient"),
                  path('update_patient_profile/', database.patient.patient_profile_image, name="patient_profile_image"),
                  path('patientprofile/', views.patientProfile, name="patientprofile"),
                  path('priscription_invoice/', database.patient.priscription_invoice, name="priscription_invoice"),
                  path('detect_disease/', database.patient.predict_disease, name="predict_disease"),
                  path('predictdisease', views.predictdisease, name="predictdisease"),
                  path('mappatient', views.map_patient, name="mappatient"),
                  path('patint_dashboard', views.patientDashboard, name="patient_dashboard"),
                  path('updateprofile', views.updateprofile, name="updateprofile"),
                  path('livecall_patient/', views.livecallPatient, name="livecall_patient"),
                  # path('patient_profile_2/', views.patient_profile_2, name="patientprofile2"),
                  path('signup/', database.patient.signup, name="patientsignup"),
                  path('payment/', database.patient.create_appointment, name="payment"),
                  path('pay_patient/', include('payments.urls')),
                  # path('doctor_profile2', views.doctor_profile2, name="doctorprofile2"),
                  # path('', views.PaymentPageView.as_view(), name='payment'),
                  # path('charge/', views.charge, name="charge"),


                  # ADMIN

                  path('mapadmin', views.map_admin, name="mapadmin"),
                  path('adminprofile', views.adminprofile, name="adminprofile"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
