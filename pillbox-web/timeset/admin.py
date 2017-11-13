# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Patient, Medicine

#class PatientAdmin(admin.ModelAdmin):
#	list_display = ('patient_name')
	
class MedicineAdmin(admin.ModelAdmin):
	list_display = ('patient', 'medicine_text', 'time')
	
admin.site.register(Patient)
admin.site.register(Medicine, MedicineAdmin)

