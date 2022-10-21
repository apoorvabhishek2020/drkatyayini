from django.contrib import admin
from .models import Patient, Medicine, PersonalHistory
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display= ['name', 'age', 'address', 'date_of_examination']

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display= ['name', 'composition']

@admin.register(PersonalHistory)
class PersonalHistoryAdmin(admin.ModelAdmin):
    list_display= ['name']