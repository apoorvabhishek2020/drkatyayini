from django.contrib import admin
from .models import Patient, Medicine
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display= ['name', 'age', 'sex', 'submission_date']

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display= ['name', 'composition']