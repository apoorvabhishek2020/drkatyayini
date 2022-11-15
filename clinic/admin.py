from django.contrib import admin
from .models import Patient, Medicine, PersonalHistory
from import_export.admin import ImportExportMixin
@admin.register(Patient)
class PatientAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display= ['name', 'age', 'address', 'date_of_examination']
    search_fields = ['name', 'age', 'address', 'date_of_examination']

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display= ['name', 'composition']
    search_fields = ['name', 'composition']

@admin.register(PersonalHistory)
class PersonalHistoryAdmin(admin.ModelAdmin):
    list_display= ['name']