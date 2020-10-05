from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class PatientsPageView(TemplateView):
    template_name = 'patients/patients.html'
