# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Patient
from django.urls import reverse

def index(request):
	patient_list = Patient.objects.order_by('patient_name')[:]
	context = {'patient_list': patient_list}
	return render(request, 'timeset/index.html', context)

def detail(request, patient_id):
	patient = get_object_or_404(Patient, pk=patient_id)
	return render(request, 'timeset/detail.html', {'patient': patient})

def results(request, patient_id):
	patient = get_object_or_404(Patient, pk=patient_id)
	return render(request, 'timeset/results.html', {'patient': patient})

def setting(request, patient_id):
	patient = get_object_or_404(Patient, pk=patient_id)
	for index, medicine in enumerate(patient.medicine_set.all()):
		s = "medicine"+str(index+1)
		medicine.time = request.POST[s]
		medicine.save()
	return HttpResponseRedirect(reverse('timeset:results', args=(patient.id,)))