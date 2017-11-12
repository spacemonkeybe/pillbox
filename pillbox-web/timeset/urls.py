from django.conf.urls import url
from . import views

app_name = 'timeset'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<patient_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<patient_id>[0-9]+)/results/$', views.results, name='results'),
	url(r'^(?P<patient_id>[0-9]+)/setting/$', views.setting, name='setting'),
]