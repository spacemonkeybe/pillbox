# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Patient
from django.urls import reverse
from django.views import generic

ip = '127.0.0.1'
from socket import *
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
    
def setip(request):
	ip = request.META.get('REMOTE_ADDR')
	print ip
	return HttpResponse(ip) 

def set(request, patient_id):
	patient = get_object_or_404(Patient, pk=patient_id)
	for index, medicine in enumerate(patient.medicine_set.all()):
		s = "medicine"+str(index+1)
		medicine.time = request.POST[s]
		medicine.save()
		HOST = ip
		PORT = 21567
		BUFSIZ = 1024
		ADDR = (HOST,PORT)
		tcpCliSock = socket(AF_INET,SOCK_STREAM)
		tcpCliSock.connect(ADDR)

		tcpCliSock.send(medicine.time)
	#message = tcpCliSock.recv(BUFSIZ)
	return HttpResponseRedirect(reverse('timeset:results', args=(patient.id,)))
	
#class PiOnline():

#def sendtime(request, patient_id):
	#pi_id = get_object_or_404(Pa)
