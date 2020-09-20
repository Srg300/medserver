from django.contrib import admin
from .models import Doctor, Recepi, Patient, Pill, Specialization

admin.site.register(Doctor)
admin.site.register(Recepi)
admin.site.register(Patient)
admin.site.register(Pill)
admin.site.register(Specialization)
