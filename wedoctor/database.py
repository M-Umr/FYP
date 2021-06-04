import self as self
from django.http import HttpResponse
import os
from tkinter import *
import numpy as np
import pandas as pd
from django.shortcuts import HttpResponse, render, redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


from .models import Patinet, Doctor
from django.contrib import messages
from django.views.generic import TemplateView
from django.views import View

from django.http import HttpResponse
import os
from tkinter import *
import numpy as np
import pandas as pd
from django.shortcuts import HttpResponse, render, redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Patinet, Doctor,Doctor_schedule,Patients_asspointment,Prescription
from django.contrib import messages
from django.views.generic import TemplateView
from django.views import View
from datetime import datetime


class person:
    def signin(request):
        if request.method == 'POST':
            email = request.POST.get('user_email', '')
            password = request.POST.get('user_password', '')
            user = authenticate(username=email, password=password)
            if user is not None:
                emails = Doctor.objects.filter(email=email)
                if len(emails) == 1:
                    login(request, user)
                    messages.success(request, 'successful login')
                    return redirect("doctors")

                login(request, user)
                messages.success(request, 'successful login')

                return redirect("patientprofile")
            else:
                messages.success(request, 'Invalio credentials login again')
                return redirect('index')

        return HttpResponse('login again')

    def __init__(self):

        self.first_name = ''
        self.last_name = ''
        self.birth_month = ''
        self.birth_day = ''
        self.birth_year = ''
        self.sex = ''
        self.contact_no = ''
        self.email = ''
        self.password = ''
        self.confirm_password = ''
        self.full_address = ''
        self.city = ''
        self.province = ''
        self.zip_cod = ''
        self.weight = 123
        self.height = 123
        self.speciliation = ''
        self.license = 123

        def setfirstname(self, request):
            self.first_name = request.POST.get('q3_name[first]', '')

        def setlastname(self, request):
            self.last_name = request.POST.get('q3_name[last]', '')

        def setbirth_month(self, request):
            self.birth_month = request.POST.get('q6_dateOf[month]', '')

        def setbirth_day(self, request):
            self.birth_day = request.POST.get('q6_dateOf[day]', '')

        def setbirth_year(self, request):
            self.birth_year = request.POST.get('q6_dateOf[year]', '')

        def setsex(self, request):
            self.sex = request.POST.get('q231_sex', '')

        def setcontact_no(self, request):
            self.contact_no = request.POST.get('q5_contactNumber[full]', '')

        def setemail(self, request):
            self.email = request.POST.get('q225_email', '')

        def setpassword(self, request):
            self.password = request.POST.get('q235_password', '')

        def setconfirm_password(self, request):
            self.confirm_password = request.POST.get('q236_confirmPassword', '')

        def setfull_address(self, request):
            self.full_address = request.POST.get('q4_address4[addr_line1]', '')

        def setcity(self, request):
            self.city = request.POST.get('q4_address4[city]', '')

        def setprovince(self, request):
            self.province = request.POST.get('q4_address4[state]', '')

        def setzip_cod(self, request):
            self.zip_cod = request.POST.get('q4_address4[postal]', '')

        def setweight(self, request):
            self.weight = request.POST.get('q119_weightkg', '')

        def setheight(self, request):
            self.height = request.POST.get('q118_heightinches118', '')


class patient(View, person):

    def signup(request):

        if request.method == "POST":
            person.first_name = request.POST.get('q3_name[first]', '')
            person.last_name = request.POST.get('q3_name[last]', '')
            person.birth_month = request.POST.get('q6_dateOf[month]', '')
            person.birth_day = request.POST.get('q6_dateOf[day]', '')
            person.birth_year = request.POST.get('q6_dateOf[year]', '')
            person.sex = request.POST.get('q231_sex', '')
            person.contact_no = request.POST.get('q5_contactNumber[full]', '')
            person.email = request.POST.get('q225_email', '')
            person.password = request.POST.get('q235_password', '')
            person.confirm_password = request.POST.get('q236_confirmPassword', '')
            person.full_address = request.POST.get('q4_address4[addr_line1]', '')
            person.city = request.POST.get('q4_address4[city]', '')
            person.province = request.POST.get('q4_address4[state]', '')
            person.zip_cod = request.POST.get('q4_address4[postal]', '')
            person.weight = request.POST.get('q119_weightkg', '')
            person.height = request.POST.get('q118_heightinches118', '')
            if person.password == person.confirm_password:
                check = User.objects.filter(username=person.email)
                if len(check) == 1:

                    return render(request, 'signupforpatient.html')

                else:
                    check = User.objects.create_user(username=person.email, email=person.email, password=person.password,
                                                     first_name=person.first_name,
                                                     last_name=person.last_name)
                    database = Patinet(first_name=person.first_name, last_name=person.last_name,
                                       birth_month=person.birth_month,
                                       birth_day=person.birth_day,
                                       birth_year=person.birth_year,
                                       sex=person.sex, contact_no=person.contact_no, email=person.email,
                                       password=person.password,
                                       confirm_password=person.confirm_password, full_address=person.full_address,
                                       city=person.city, province=person.province, zip_cod=person.zip_cod,
                                       weight=person.weight, height=person.height)
                    database.save();
                    messages.success(request, 'Signup Successfully Done!')

                    return render(request, 'index.html')
            else:
                return HttpResponse("Password and confirm password are not same")

        return render(request, 'index.html')

    def patient_profile_image(request):
        image_file = request.FILES['profile_image']
        current_user = request.user
        patient = Patinet.objects.get(email=current_user)
        patient.image=image_file
        patient.save()

        return redirect('updateprofile')

    def create_appointment(request):
        if request.method == "POST":
            day = request.POST.get('day', '')
            time = request.POST.get('time', '')
            doc=request.POST.get('doctor','')


            Appointment=appointment()
            Appointment.bookappointment(request,day,time,doc)
            doctor = Doctor.objects.get(email=doc)



        return render(request, 'payment.html',{'day':day,'time':time,'doctor':doctor})

    def priscription_invoice(request):

        if request.method == "POST":
            patient_email = request.POST.get('patient_email', '')
            doctor_email = request.POST.get('doctor_email', '')
            date = request.POST.get('date', '')
            appointment_day = request.POST.get('appointment_day', '')
            appointment_time = request.POST.get('appointment_time', '')
            prescription = Prescription.objects.filter(patient_email=patient_email, doctor_email=doctor_email,
                                                               date=date, appointment_day=appointment_day,
                                                               appointment_time=appointment_time)


            return render(request, 'priscription_invoice.html',{'prescription':prescription[0]})

    def predict_disease(request):

        if request.method == "POST":

            ppsymptoms = request.POST.get('four', '')

            psymptoms = ppsymptoms.split(',')
            print(psymptoms)

            symptoms_list1 = ['itching', 'skin_rash', 'continuous_sneezing', 'shivering', 'stomach_pain', 'acidity',
                              'vomiting',
                              'indigestion',
                              'muscle_wasting', 'patches_in_throat', 'fatigue', 'weight_loss', 'sunken_eyes', 'cough',
                              'headache', 'chest_pain',
                              'back_pain', 'weakness_in_limbs', 'chills', 'joint_pain', 'yellowish_skin',
                              'constipation',
                              'pain_during_bowel_movements',
                              'breathlessness', 'cramps', 'weight_gain', 'mood_swings', 'neck_pain', 'muscle_weakness',
                              'stiff_neck', 'pus_filled_pimples',
                              'burning_micturition', 'bladder_discomfort', 'high_fever', 'nodal_skin_eruptions',
                              'ulcers_on_tongue', 'loss_of_appetite',
                              'restlessness', 'dehydration', 'dizziness', 'weakness_of_one_body_side', 'lethargy',
                              'nausea',
                              'abdominal_pain',
                              'pain_in_anal_region', 'sweating', 'bruising', 'cold_hands_and_feets', 'anxiety',
                              'knee_pain',
                              'swelling_joints',
                              'blackheads', 'foul_smell_of urine', 'skin_peeling', 'blister', 'dischromic _patches',
                              'watering_from_eyes', 'extra_marital_contacts',
                              'diarrhoea', 'loss_of_balance', 'blurred_and_distorted_vision', 'altered_sensorium',
                              'dark_urine',
                              'swelling_of_stomach', 'bloody_stool', 'obesity',
                              'hip_joint_pain', 'movement_stiffness', 'spinning_movements', 'scurring',
                              'continuous_feel_of_urine', 'silver_like_dusting', 'red_sore_around_nose',
                              'spotting_ urination', 'passage_of_gases', 'irregular_sugar_level', 'family_history',
                              'lack_of_concentration', 'excessive_hunger', 'yellowing_of_eyes',
                              'distention_of_abdomen', 'irritation_in_anus', 'swollen_legs', 'painful_walking',
                              'small_dents_in_nails', 'yellow_crust_ooze',
                              'internal_itching', 'mucoid_sputum', 'history_of_alcohol_consumption',
                              'swollen_blood_vessels',
                              'unsteadiness', 'inflammatory_nails',
                              'depression', 'fluid_overload', 'swelled_lymph_nodes', 'malaise',
                              'prominent_veins_on_calf',
                              'puffy_face_and_eyes', 'fast_heart_rate', 'irritability',
                              'muscle_pain', 'mild_fever', 'yellow_urine', 'phlegm', 'enlarged_thyroid',
                              'increased_appetite',
                              'visual_disturbances', 'brittle_nails', 'drying_and_tingling_lips',
                              'polyuria', 'pain_behind_the_eyes', 'toxic_look_(typhos)', 'throat_irritation',
                              'swollen_extremeties', 'slurred_speech', 'red_spots_over_body',
                              'belly_pain', 'receiving_blood_transfusion', 'acute_liver_failure', 'redness_of_eyes',
                              'rusty_sputum', 'abnormal_menstruation', 'receiving_unsterile_injections', 'coma',
                              'sinus_pressure', 'palpitations', 'stomach_bleeding', 'runny_nose', 'congestion',
                              'blood_in_sputum', 'loss_of_smell']
            data = pd.read_csv(r"dataset.csv")
            disease = []
            for d1 in range(0, len(data)):
                a = data.iloc[d1, 0]
                if a not in disease:
                    disease.append(a)

            l2 = []
            for x in range(0, len(symptoms_list1)):
                l2.append(0)

            df = pd.read_csv("csvexample3.csv")
            index = 0
            for i in range(0, len(disease)):
                df.replace(
                    {'diseases': {i: index}}, inplace=True)
                index = index + 1
            print(df)
            # features
            x = df[symptoms_list1]
            # target values
            y = df[["diseases"]]
            from sklearn.ensemble import RandomForestClassifier
            from sklearn.model_selection import train_test_split
            X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
            # random forest k sub trees
            random_forest_object = RandomForestClassifier(n_estimators=100)
            random_forest_object.fit(X_train, y_train)
            # calculating accuracy-
            from sklearn.metrics import accuracy_score
            y_pred = random_forest_object.predict(X_test)
            print(accuracy_score(y_test, y_pred))
            print(accuracy_score(y_test, y_pred, normalize=False))
            for k in range(0, len(symptoms_list1)):
                for z in psymptoms:
                    if (z == symptoms_list1[k]):
                        l2[k] = 1

            inputtest = [l2]
            predict = random_forest_object.predict(inputtest)
            predicted = predict[0]
            print(predicted)

            yes = 'yes'
            doctors = Doctor.objects.filter(spc=predicted)
            if len(doctors) >= 1:
                do = 'yes'

            else:
                do = 'no'

            a_list = []
            # predicted disease k unique symptoms
            for d1 in range(0, len(data)):
                # print(d1)
                if data.iloc[d1, 0] == predicted:
                    for x in range(1, 17):
                        sym = data.iloc[d1, x]
                        if sym not in a_list:
                            a_list.append(sym)
            blist = []
            match_symptom_count = []
            not_match_symptoms = []
            disease_symptoms = [x for x in a_list if str(x) != 'nan']
            for i in disease_symptoms:
                i = i.replace(" ", "")
                blist.append(i)

            for symptom in psymptoms:

                if symptom in blist:
                    if symptom not in match_symptom_count:
                        print(symptom)
                        match_symptom_count.append(symptom)

            for index in blist:
                if index not in psymptoms:
                    not_match_symptoms.append(index)

            percentage = len(match_symptom_count) / len(blist)
            percentage = percentage * 100
            percentage = round(percentage, 0)

            if percentage <= 40:
                yes = 'no'
                do = 'no'

            return render(request, 'predict_disease.html',
                          {'b': predicted, 'doctors': doctors, 'yes': yes, 'do': do, 'percentage': percentage,
                           'not_match_symptoms': not_match_symptoms})



























class doctor(View,person):
    def signupfordoctors(request):
        if request.method == "POST":
            person.first_name = request.POST.get('q3_name[first]', '')
            person.last_name = request.POST.get('q3_name[last]', '')
            person.birth_month = request.POST.get('q6_dateOf[month]', '')
            person.birth_day = request.POST.get('q6_dateOf[day]', '')
            person.birth_year = request.POST.get('q6_dateOf[year]', '')
            person.sex = request.POST.get('q231_sex', '')
            person.contact_no = request.POST.get('q5_contactNumber[full]', '')
            person.email = request.POST.get('q225_email', '')
            person.password = request.POST.get('q235_password', '')
            person.confirm_password = request.POST.get('q236_confirmPassword', '')
            person.full_address = request.POST.get('q4_address4[addr_line1]', '')
            person.city = request.POST.get('q4_address4[city]', '')
            person.province = request.POST.get('q4_address4[state]', '')
            person.zip_cod = request.POST.get('q4_address4[postal]', '')
            person.speciliation = request.POST.get('input_237', '')
            person.license = request.POST.get('q118_licenseNumber', '')
            if person.password == person.confirm_password:
                check = User.objects.filter(username=person.email)
                if len(check) == 1:
                    messages.warning(request, 'user is already exits with this email address')
                    return render(request, 'signupfordoctor.html')

                else:

                    database = Doctor(first_name=person.first_name, last_name=person.last_name,
                                      birth_month=person.birth_month,
                                      birth_day=person.birth_day,
                                      birth_year=person.birth_year,
                                      sex=person.sex, contact_no=person.contact_no, email=person.email,
                                      password=person.password,
                                      confirm_password=person.confirm_password, full_address=person.full_address,
                                      city=person.city, province=person.province, zip_cod=person.zip_cod,
                                      spc=person.speciliation, license=person.license)
                    database.save();
                    check = User.objects.create_user(username=person.email, email=person.email,
                                                     password=person.password,
                                                     first_name=person.first_name,
                                                     last_name=person.last_name)
                    return render(request, 'index.html')

            else:
                return HttpResponse("Password and confirm password are not same")


        return render(request, 'signupfordoctor.html')



    def set_appointments(request):
        schedule_doctor_object=schedule_doctor()
        ack=schedule_doctor_object.addschedule(request)
        if ack==1:
            email = request.user
            print("12346")
            get_doctor_schedule = Doctor_schedule.objects.filter(doctor_email=email)
            if len(get_doctor_schedule) > 0:

                monday_schedule1 = Doctor_schedule.objects.filter(doctor_email=email, monday='Monday',
                                                                  appointment_slot='1')
                monday_schedule2 = Doctor_schedule.objects.filter(doctor_email=email, monday='Monday',
                                                                  appointment_slot='2')
                monday_schedule3 = Doctor_schedule.objects.filter(doctor_email=email, monday='Monday',
                                                                  appointment_slot='3')
                tuesday_schedule1 = Doctor_schedule.objects.filter(doctor_email=email, tuesday='Tuesday',
                                                                   appointment_slot='1')
                tuesday_schedule2 = Doctor_schedule.objects.filter(doctor_email=email, tuesday='Tuesday',
                                                                   appointment_slot='2')
                tuesday_schedule3 = Doctor_schedule.objects.filter(doctor_email=email, tuesday='Tuesday',
                                                                   appointment_slot='3')
                wednesday_schedule1 = Doctor_schedule.objects.filter(doctor_email=email, wednesday='Wednesday',
                                                                     appointment_slot='1')
                wednesday_schedule2 = Doctor_schedule.objects.filter(doctor_email=email, wednesday='Wednesday',
                                                                     appointment_slot='2')
                wednesday_schedule3 = Doctor_schedule.objects.filter(doctor_email=email, wednesday='Wednesday',
                                                                     appointment_slot='3')
                thursday_schedule1 = Doctor_schedule.objects.filter(doctor_email=email, thursday='Thursday',
                                                                    appointment_slot='1')
                thursday_schedule2 = Doctor_schedule.objects.filter(doctor_email=email, thursday='Thursday',
                                                                    appointment_slot='2')
                thursday_schedule3 = Doctor_schedule.objects.filter(doctor_email=email, thursday='Thursday',
                                                                    appointment_slot='3')
                friday_schedule1 = Doctor_schedule.objects.filter(doctor_email=email, friday='Friday',
                                                                  appointment_slot='1')
                friday_schedule2 = Doctor_schedule.objects.filter(doctor_email=email, friday='Friday',
                                                                  appointment_slot='2')
                friday_schedule3 = Doctor_schedule.objects.filter(doctor_email=email, friday='Friday',
                                                                  appointment_slot='3')
                saturday_schedule1 = Doctor_schedule.objects.filter(doctor_email=email, saturday='Saturday',
                                                                    appointment_slot='1')
                saturday_schedule2 = Doctor_schedule.objects.filter(doctor_email=email, saturday='Saturday',
                                                                    appointment_slot='2')
                saturday_schedule3 = Doctor_schedule.objects.filter(doctor_email=email, saturday='Saturday',
                                                                    appointment_slot='3')
                sunday_schedule1 = Doctor_schedule.objects.filter(doctor_email=email, sunday='Sunday',
                                                                  appointment_slot='1')
                sunday_schedule2 = Doctor_schedule.objects.filter(doctor_email=email, sunday='Sunday',
                                                                  appointment_slot='2')
                sunday_schedule3 = Doctor_schedule.objects.filter(doctor_email=email, sunday='Sunday',
                                                                  appointment_slot='3')

                return render(request, 'calendar.html',
                              {'monday_schedule1': monday_schedule1, 'monday_schedule2': monday_schedule2,
                               'monday_schedule3': monday_schedule3, 'tuesday_schedule1': tuesday_schedule1,
                               'tuesday_schedule2': tuesday_schedule2, 'tuesday_schedule3': tuesday_schedule3,
                               'wednesday_schedule1': wednesday_schedule1, 'wednesday_schedule2': wednesday_schedule2,
                               'wednesday_schedule3': wednesday_schedule3, 'thursday_schedule1': thursday_schedule1,
                               'thursday_schedule2': thursday_schedule2,
                               'thursday_schedule3': thursday_schedule3, 'friday_schedule1': friday_schedule1,
                               'friday_schedule2': friday_schedule2,
                               'friday_schedule3': friday_schedule3, 'saturday_schedule1': saturday_schedule1,
                               'saturday_schedule2': saturday_schedule2,
                               'saturday_schedule3': saturday_schedule3, 'sunday_schedule1': sunday_schedule1,
                               'sunday_schedule2': sunday_schedule2, 'sunday_schedule3': sunday_schedule3})
            else:
                return render(request, 'calendar.html')
        else:
         return render(request, 'calendar.html')



    def accept_appointment(request):
        if request.method == "POST":
            current_user = request.user
            patients = Patients_asspointment.objects.filter(doctor_email=current_user)
            doctor = Doctor.objects.filter(email=current_user)
            patient_email = request.POST.get('accept_patient_email', '')
            appointment_time = request.POST.get('appointment_time', '')
            appointment_day = request.POST.get('appointment_day', '')
            appointment_daytime = request.POST.get('datetime', '')


            app=appointment()
            app.accept_appointment_patient(request,patient_email,appointment_time,appointment_day,appointment_daytime)




            return render(request, 'appointment_requests_doctor.html', {'doctor': doctor[0], 'patients': patients})

    def cancel_appointment(request):
        if request.method == "POST":
            current_user = request.user
            patients = Patients_asspointment.objects.filter(doctor_email=current_user)
            doctor = Doctor.objects.filter(email=current_user)
            patient_email = request.POST.get('cancel_patient_email', '')
            appointment_time = request.POST.get('appointmentt_time', '')
            appointment_day = request.POST.get('appointmentt_day', '')
            appointment_daytime = request.POST.get('datettime', '')
            app = appointment()
            app.cancel_appointment_patient(request,patient_email,appointment_time,appointment_day,appointment_daytime)

            return render(request, 'appointment_requests_doctor.html', {'doctor': doctor[0], 'patients': patients})



    def prescribemedicine(request):

        if request.method == "POST":
            medicine = request.POST.get('mytext[]','')
            time = request.POST.getlist('time','')
            disease = request.POST.get('disease','')
            quantity = request.POST.get('quantity[]','')
            days = request.POST.get('days[]','')
            appointment_day = request.POST.get('appointment_day','')
            appointment_time = request.POST.get('appointment_time','')
            date = request.POST.get('date','')
            patient_email = request.POST.get('patient_email', '')
            doctor_email = request.POST.get('doctor_email', '')
            instructions = request.POST.get('instructions', '')
            print(instructions)



            object = prescription()
            object.addprescription(request, medicine, time, disease, quantity, days, appointment_day, appointment_time,
                                   date, patient_email, doctor_email,instructions)





            return render(request, 'appointment_requests_doctor.html')

    def view_patient_history(request):

        if request.method=="POST":

           patient_email= request.POST.get('view_patient_email', '')
           appointment_day = request.POST.get('view_appointment_day', '')
           appointment_time = request.POST.get('view_appointment_time', '')
           datetime = request.POST.get('view_datetime', '')
           patient = Patients_asspointment.objects.filter(patient_email=patient_email)
           profile = Patinet.objects.filter(email=patient_email)
           # object = history()
           # object.patient_medical_history(request,patient_email,appointment_day,appointment_time,datetime)


        return render(request, 'patient_medical_history.html',{'patient':patient,'profile':profile[0]})


















class schedule_doctor:

    def __init__(self):
        self.appointment_slot =''
        self.monday =''
        self.tuesday =''
        self.wednesday =''
        self.thursday =''
        self.friday =''
        self.saturday =''
        self.sunday =''
        self.start_time =''
        self.end_time =''
        self.availability =''


    def addschedule(self,request):
        if request.method == "POST":

            appointment_slot = request.POST.get('slot', '')
            scheduleday = request.POST.get('scheduleday', '')
            start_time = request.POST.get('starttime', '')
            end_time = request.POST.get('endtime', '')
            availability = request.POST.get('bookavail', '')
            check_monday = Doctor_schedule.objects.filter(doctor_email=request.user,appointment_slot=appointment_slot,monday=scheduleday)
            check_tuesday = Doctor_schedule.objects.filter(doctor_email=request.user, appointment_slot=appointment_slot,tuesday=scheduleday)
            check_wednesday = Doctor_schedule.objects.filter(doctor_email=request.user, appointment_slot=appointment_slot,wednesday=scheduleday)
            check_thursday = Doctor_schedule.objects.filter(doctor_email=request.user, appointment_slot=appointment_slot,thursday=scheduleday)
            check_friday = Doctor_schedule.objects.filter(doctor_email=request.user, appointment_slot=appointment_slot,friday=scheduleday)
            check_saturday = Doctor_schedule.objects.filter(doctor_email=request.user, appointment_slot=appointment_slot,saturday=scheduleday)
            check_sunday = Doctor_schedule.objects.filter(doctor_email=request.user,appointment_slot=appointment_slot, sunday=scheduleday)

            if len(check_monday)>0:
                Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=request.user,appointment_slot=appointment_slot,monday=scheduleday)
                Doctor_schedule_object.start_time=start_time
                Doctor_schedule_object.end_time = end_time
                Doctor_schedule_object.availability = availability
                Doctor_schedule_object.save()
                print("check_monday")
                return 1
            elif  len(check_tuesday)>0:
                Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=request.user,
                                                                     appointment_slot=appointment_slot,
                                                                     tuesday=scheduleday)
                Doctor_schedule_object.start_time = start_time
                Doctor_schedule_object.end_time = end_time
                Doctor_schedule_object.availability = availability
                Doctor_schedule_object.save()
                print("check_tuesday")
                return 1

            elif len(check_wednesday) > 0:
                Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=request.user,
                                                                     appointment_slot=appointment_slot,
                                                                     wednesday=scheduleday)
                Doctor_schedule_object.start_time = start_time
                Doctor_schedule_object.end_time = end_time
                Doctor_schedule_object.availability = availability
                Doctor_schedule_object.save()
                print("check_wednesday")
                return 1

            elif len(check_thursday) > 0:
                Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=request.user,
                                                                     appointment_slot=appointment_slot,
                                                                     thursday=scheduleday)
                Doctor_schedule_object.start_time = start_time
                Doctor_schedule_object.end_time = end_time
                Doctor_schedule_object.availability = availability
                Doctor_schedule_object.save()
                print("check_thursday")
                return 1
            elif len(check_friday) > 0:
                Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=request.user,
                                                                     appointment_slot=appointment_slot,
                                                                     friday=scheduleday)
                Doctor_schedule_object.start_time = start_time
                Doctor_schedule_object.end_time = end_time
                Doctor_schedule_object.availability = availability
                Doctor_schedule_object.save()
                print("check_friday")
                return 1

            elif len(check_saturday) > 0:
                Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=request.user,
                                                                     appointment_slot=appointment_slot,
                                                                     saturday=scheduleday)
                Doctor_schedule_object.start_time = start_time
                Doctor_schedule_object.end_time = end_time
                Doctor_schedule_object.availability = availability
                Doctor_schedule_object.save()
                print("check_saturday")
                return 1




            elif len(check_sunday) > 0:
                Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=request.user,
                                                                     appointment_slot=appointment_slot,
                                                                     sunday=scheduleday)
                Doctor_schedule_object.start_time = start_time
                Doctor_schedule_object.end_time = end_time
                Doctor_schedule_object.availability = availability
                Doctor_schedule_object.save()
                print("check_sunday")
                return 1


            else:
                print("else")
                if scheduleday=='Monday':
                 add_new_schedule_object=Doctor_schedule(doctor_email=request.user,first_name=request.user.first_name,last_name=request.user.last_name,appointment_slot=appointment_slot,monday=scheduleday,start_time=start_time,end_time=end_time,availability=availability)
                 add_new_schedule_object.save()
                 print("elsemonday")
                 return 1


                 return 1
                elif scheduleday =='Tuesday':
                    add_new_schedule_object = Doctor_schedule(doctor_email=request.user,
                                                              first_name=request.user.first_name,
                                                              last_name=request.user.last_name,
                                                              appointment_slot=appointment_slot, tuesday=scheduleday,
                                                              start_time=start_time, end_time=end_time,
                                                              availability=availability)
                    add_new_schedule_object.save()
                    print("elsetuesday")
                    return 1

                elif scheduleday =='Wednesday':
                    add_new_schedule_object = Doctor_schedule(doctor_email=request.user,
                                                              first_name=request.user.first_name,
                                                              last_name=request.user.last_name,
                                                              appointment_slot=appointment_slot, wednesday=scheduleday,
                                                              start_time=start_time, end_time=end_time,
                                                              availability=availability)
                    add_new_schedule_object.save()
                    print("elsewednesday")
                    return 1

                elif scheduleday == 'Thursday':
                    add_new_schedule_object = Doctor_schedule(doctor_email=request.user,
                                                              first_name=request.user.first_name,
                                                              last_name=request.user.last_name,
                                                              appointment_slot=appointment_slot, thursday=scheduleday,
                                                              start_time=start_time, end_time=end_time,
                                                              availability=availability)
                    add_new_schedule_object.save()
                    print("elsethursday")
                    return 1
                elif scheduleday == 'Friday':
                    add_new_schedule_object = Doctor_schedule(doctor_email=request.user,
                                                              first_name=request.user.first_name,
                                                              last_name=request.user.last_name,
                                                              appointment_slot=appointment_slot, friday=scheduleday,
                                                              start_time=start_time, end_time=end_time,
                                                              availability=availability)
                    add_new_schedule_object.save()
                    print("elsefriday")
                    return 1
                elif scheduleday == 'Saturday':
                    add_new_schedule_object = Doctor_schedule(doctor_email=request.user,
                                                              first_name=request.user.first_name,
                                                              last_name=request.user.last_name,
                                                              appointment_slot=appointment_slot, saturday=scheduleday,
                                                              start_time=start_time, end_time=end_time,
                                                              availability=availability)
                    add_new_schedule_object.save()
                    print("elsesaturday")
                    return 1

                elif scheduleday == 'Sunday':
                    add_new_schedule_object = Doctor_schedule(doctor_email=request.user,
                                                              first_name=request.user.first_name,
                                                              last_name=request.user.last_name,
                                                              appointment_slot=appointment_slot, sunday=scheduleday,
                                                              start_time=start_time, end_time=end_time,
                                                              availability=availability)
                    add_new_schedule_object.save()
                    print("elsesunday")
                    return 1

                else:
                    print("error")
                    return 0



class appointment(View):
    def __init__(self):
       self.patient_id =""
       self.patient_email =""
       self.doctor_email =""
       self.appointment_status=""
       self.booking_date =""
       self.appointment_day =""
       self.amount = ""
       self.appointment_time=""
       self.doctor_first_name=""
       self.doctor_last_name=""
       self.patient_first_name = ""
       self.patient_last_name = ""
       self.patient_city = ""
       self.patient_province = ""
       self.patient_contact_no = ""
       self.date=""
       self.patient_image=""
       self.doctor_image = ""
       self.doctor_spec = ""


    def bookappointment(self,request,day,time,doc):
        doctor = Doctor.objects.filter(email=doc)
        patient = Patinet.objects.filter(email=request.user)



        self.patient_email = request.user
        self.doctor_email=doc
        self.appointment_status="pending"
        self.booking_date=datetime.today()
        self.appointment_day=day
        self.appointment_time=time
        self.amount="2000"
        self.doctor_first_name=doctor[0].first_name
        self.doctor_last_name=doctor[0].last_name
        self.doctor_image =doctor[0].image
        self.doctor_spec=doctor[0].spc
        self.patient_first_name = patient[0].first_name
        self.patient_last_name = patient[0].last_name
        self.patient_image = patient[0].image
        self.patient_city = patient[0].city
        self.patient_province = patient[0].province
        self.patient_contact_no = patient[0].contact_no
        self.date=datetime.today().strftime("%m/%d/%Y, %H:%M:%S")






        patients_asspointment = Patients_asspointment(patient_email=self.patient_email,
                                                  doctor_email=self.doctor_email,patient_first_name=self.patient_first_name,
                                                  patient_last_name=self.patient_last_name,patient_city=self.patient_city,
                                                  patient_province=self.patient_province,patient_contact_no=self.patient_contact_no,
                                                  appointment_status=self.appointment_status,
                                                  booking_date=self.booking_date, appointment_day= self.appointment_day,
                                                  amount= self.amount, doctor_first_name=self.doctor_first_name,
                                                  doctor_last_name=self.doctor_last_name,
                                                  appointment_time=self.appointment_time,date=self.date,patient_image= self.patient_image,doctor_image = self.doctor_image,doctor_spec=self.doctor_spec )
        patients_asspointment.save()


        if self.appointment_day == 'Monday':
            print("check_monday")
            Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=self.doctor_email,
                                                                 start_time=self.appointment_time, monday=self.appointment_day)
            Doctor_schedule_object.availability = "notavailable"
            Doctor_schedule_object.save()


        elif self.appointment_day == 'Tuesday':

            Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=self.doctor_email,
                                                                 start_time=self.appointment_time,
                                                                 tuesday=self.appointment_day)

            Doctor_schedule_object.availability = "notavailable"
            Doctor_schedule_object.save()
            print("check_monday")


        elif self.appointment_day == 'Wednesday':
            Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=self.doctor_email,
                                                                 start_time=self.appointment_time,
                                                                 wednesday=self.appointment_day)

            Doctor_schedule_object.availability = "notavailable"
            Doctor_schedule_object.save()
            print("check_monday")


        elif self.appointment_day == 'Thursday':
            Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=self.doctor_email,
                                                                 start_time=self.appointment_time,
                                                                 thursday=self.appointment_day)

            Doctor_schedule_object.availability = "notavailable"
            Doctor_schedule_object.save()
            print("check_monday")

        elif self.appointment_day == 'Friday':

            Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=self.doctor_email,
                                                                 start_time=self.appointment_time,
                                                                 friday=self.appointment_day)
            Doctor_schedule_object.availability = "notavailable"
            Doctor_schedule_object.save()
            print("check_monday")

        elif self.appointment_day == 'Saturday':
            Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=self.doctor_email,
                                                                 start_time=self.appointment_time,
                                                                 saturday=self.appointment_day)

            Doctor_schedule_object.availability = "notavailable"
            Doctor_schedule_object.save()
            print("check_monday")


        elif self.appointment_day == 'Sunday':
            Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=self.doctor_email,
                                                                 start_time=self.appointment_time,
                                                                 sunday=self.appointment_day)

            Doctor_schedule_object.availability = "notavailable"
            Doctor_schedule_object.save()
            print("check_monday")


        else:

            print("error")





        return render(request,'payment.html',{'doctor':doctor[0],'patient':patient[0],'day':day,'time':time,'doc':doc})



    def accept_appointment_patient(self,request,patient_email,appointment_time,appointment_day,appointment_daytime):
        print(appointment_daytime)
        print("ihtasham")

        pa_appointment = Patients_asspointment.objects.get(patient_email=patient_email, appointment_time=appointment_time,
                                                    appointment_day=appointment_day,date=appointment_daytime)

        pa_appointment.appointment_status ="accept"

        pa_appointment.save()

        current_user = request.user
        patients = Patients_asspointment.objects.filter(doctor_email=current_user)
        doctor = Doctor.objects.filter(email=current_user)

        return render(request, 'appointment_requests_doctor.html', {'doctor': doctor[0], 'patients': patients})



    def cancel_appointment_patient(self,request,patient_email,appointment_time,appointment_day,appointment_daytime):
            self.appointment_day=appointment_day
            self.doctor_email=request.user
            self.appointment_time=appointment_time




            pa_appointment = Patients_asspointment.objects.get(patient_email=patient_email,
                                                               appointment_time=appointment_time,
                                                               appointment_day=appointment_day,
                                                               date=appointment_daytime)

            pa_appointment.appointment_status = "cancelled"

            pa_appointment.save()

            current_user = request.user
            patients = Patients_asspointment.objects.filter(doctor_email=current_user)
            doctor = Doctor.objects.filter(email=current_user)


            if self.appointment_day == 'Monday':
                print("check_monday")
                Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=self.doctor_email,
                                                                     start_time=self.appointment_time,
                                                                     monday=self.appointment_day)
                Doctor_schedule_object.availability = "available"
                Doctor_schedule_object.save()


            elif self.appointment_day == 'Tuesday':
                Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=self.doctor_email,
                                                                     start_time=self.appointment_time,
                                                                     tuesday=self.appointment_day)

                Doctor_schedule_object.availability = "available"
                Doctor_schedule_object.save()
                print("check_monday")


            elif self.appointment_day == 'Wednesday':
                Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=self.doctor_email,
                                                                     start_time=self.appointment_time,
                                                                     wednesday=self.appointment_day)

                Doctor_schedule_object.availability = "available"
                Doctor_schedule_object.save()
                print("check_monday")


            elif self.appointment_day == 'Thursday':
                Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=self.doctor_email,
                                                                     start_time=self.appointment_time,
                                                                     thursday=self.appointment_day)

                Doctor_schedule_object.availability = "available"
                Doctor_schedule_object.save()
                print("check_monday")

            elif self.appointment_day == 'Friday':
                Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=self.doctor_email,
                                                                     start_time=self.appointment_time,
                                                                     friday=self.appointment_day)

                Doctor_schedule_object.availability = "available"
                Doctor_schedule_object.save()
                print("check_monday")

            elif self.appointment_day == 'Saturday':
                Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=self.doctor_email,
                                                                     start_time=self.appointment_time,
                                                                     saturday=self.appointment_day)

                Doctor_schedule_object.availability = "available"
                Doctor_schedule_object.save()
                print("check_monday")


            elif self.appointment_day == 'Sunday':
                Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=self.doctor_email,
                                                                     start_time=self.appointment_time,
                                                                     sunday=self.appointment_day)

                Doctor_schedule_object.availability = "available"
                Doctor_schedule_object.save()
                print("check_monday")


            else:

                print("error")

            return render(request, 'appointment_requests_doctor.html', {'doctor': doctor[0], 'patients': patients})





class prescription(View):

    def __init__(self):

        self.patient_id =""
        self.patient_email =""
        self.doctor_email =""
        self.appointment_status =""
        self.booking_date =""
        self.appointment_day =""
        self.amount =""
        self.appointment_time =""
        self.doctor_first_name =""
        self.doctor_last_name =""
        self.patient_first_name =""
        self.patient_last_name =""
        self.patient_city =""
        self.patient_province =""
        self.patient_contact_no =""
        self.date =""
        self.patient_image =""
        self.doctor_image =""
        self.medicine =""
        self.time =""
        self.disease =""
        self.quantity =""
        self.days =""
        self.prescription_date=""
        self.instructions=""







    def addprescription(self,request,medicine, time, disease, quantity, days, appointment_day, appointment_time,
                                   date, patient_email, doctor_email,instructions):



        if request.method == "POST":
            current_user = request.user

            doctor = Doctor.objects.filter(email=current_user)


            doctor = Doctor.objects.filter(email=doctor_email)
            patient = Patinet.objects.filter(email=patient_email)
            patient_app = Patients_asspointment.objects.filter(patient_email=patient_email, doctor_email=doctor_email,
                                                               date=date, appointment_day=appointment_day,
                                                               appointment_time=appointment_time)

            self.patient_email = patient_email
            self.doctor_email = doctor_email
            self.booking_date = patient_app[0].booking_date
            self.appointment_day = patient_app[0].appointment_day
            self.appointment_time = patient_app[0].appointment_time
            self.doctor_first_name = patient_app[0].doctor_first_name
            self.doctor_last_name = patient_app[0].doctor_last_name
            self.doctor_image = patient_app[0].doctor_image
            self.patient_first_name = patient_app[0].patient_first_name
            self.patient_last_name = patient_app[0].patient_last_name
            self.patient_image = patient_app[0].patient_image
            self.patient_city = patient_app[0].patient_city
            self.patient_province = patient_app[0].patient_province
            self.patient_contact_no = patient_app[0].patient_contact_no
            self.date = patient_app[0].date
            self.medicine=medicine
            self.time=time
            self.disease=disease
            self.quantity=quantity
            self.days=days
            self.prescription_date=datetime.today().strftime("%m/%d/%Y")
            self.instructions=instructions



            pre=Prescription(patient_email=self.patient_email,patient_first_name=self.patient_first_name,patient_last_name=self.patient_last_name,
                             patient_city=self.patient_city,patient_province=self.patient_province,patient_contact_no=self.patient_contact_no,
                             doctor_email=self.doctor_email,booking_date=self.booking_date,appointment_day=self.appointment_day,doctor_first_name=self.doctor_first_name,
                             doctor_last_name=self.doctor_last_name,appointment_time=self.appointment_time,date=self.date,doctor_image=self.doctor_image,
                             medicine=self.medicine,time=self.time,disease=self.disease,quantity=self.quantity,days=self.days,prescription_date=self.prescription_date,instructions=self.instructions)
            pre.save()

            pa_appointment = Patients_asspointment.objects.get(patient_email=patient_email, doctor_email=doctor_email,
                                                               date=date, appointment_day=appointment_day,
                                                               appointment_time=appointment_time)
            pa_appointment.appointment_status = "done"
            pa_appointment.prescription_date =self.prescription_date
            pa_appointment.save()



            if self.appointment_day == 'Monday':
                print("check_monday")
                Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=self.doctor_email,
                                                                     start_time=self.appointment_time,
                                                                     monday=self.appointment_day)
                Doctor_schedule_object.availability = "available"
                Doctor_schedule_object.save()


            elif self.appointment_day == 'Tuesday':
                Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=self.doctor_email,
                                                                     start_time=self.appointment_time,
                                                                     tuesday=self.appointment_day)

                Doctor_schedule_object.availability = "available"
                Doctor_schedule_object.save()
                print("check_monday")


            elif self.appointment_day == 'Wednesday':
                Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=self.doctor_email,
                                                                     start_time=self.appointment_time,
                                                                     wednesday=self.appointment_day)

                Doctor_schedule_object.availability = "available"
                Doctor_schedule_object.save()
                print("check_monday")


            elif self.appointment_day == 'Thursday':
                Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=self.doctor_email,
                                                                     start_time=self.appointment_time,
                                                                     thursday=self.appointment_day)

                Doctor_schedule_object.availability = "available"
                Doctor_schedule_object.save()
                print("check_monday")

            elif self.appointment_day == 'Friday':
                Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=self.doctor_email,
                                                                     start_time=self.appointment_time,
                                                                     friday=self.appointment_day)

                Doctor_schedule_object.availability = "available"
                Doctor_schedule_object.save()
                print("check_monday")

            elif self.appointment_day == 'Saturday':
                Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=self.doctor_email,
                                                                     start_time=self.appointment_time,
                                                                     saturday=self.appointment_day)

                Doctor_schedule_object.availability = "available"
                Doctor_schedule_object.save()
                print("check_monday")


            elif self.appointment_day == 'Sunday':
                Doctor_schedule_object = Doctor_schedule.objects.get(doctor_email=self.doctor_email,
                                                                     start_time=self.appointment_time,
                                                                     sunday=self.appointment_day)

                Doctor_schedule_object.availability = "available"
                Doctor_schedule_object.save()
                print("check_monday")


            else:

                print("error")

            return render(request, 'appointment_requests_doctor.html')


class history(View):
    def __init__(self):
        self.patient_email = ""
        self.appointment_day =""
        self.appointment_time=""
        self.datetime=""



    def patient_medical_history(self,request,patient_email,appointment_day,appointment_time,datetime):
        if request.method == "POST":

            return render(request, 'patient_medical_history.html')






