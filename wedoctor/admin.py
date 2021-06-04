from django.contrib import admin

# Register your models here.


from .models import Patinet,Doctor,Doctor_schedule,Patients_asspointment,Prescription

admin.site.register(Patinet)
admin.site.register(Doctor)
admin.site.register(Doctor_schedule)
admin.site.register(Patients_asspointment)
admin.site.register(Prescription)

