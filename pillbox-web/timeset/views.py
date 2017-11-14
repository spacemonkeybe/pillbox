# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Patient
from django.urls import reverse
from django.views import generic

class IndexView(generic.ListView):
	template_name = 'timeset/index.html'
	context_object_name = 'patient_list'
	def get_queryset(self):
		return Patient.objects.all()

class ResultsView(generic.DetailView):
	model = Patient
	template_name = 'timeset/results.html'

class SettingView(generic.DetailView):
	model = Patient
	template_name = 'timeset/setting.html'

def Login(request):
    return render(request, 'timeset/login.html')

def set(request, patient_id):
	patient = get_object_or_404(Patient, pk=patient_id)
	for index, medicine in enumerate(patient.medicine_set.all()):
		s = "medicine"+str(index+1)
		medicine.time = request.POST[s]
		medicine.save()
	return HttpResponseRedirect(reverse('timeset:results', args=(patient.id,)))