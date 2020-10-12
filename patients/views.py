from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from patients.forms import PatientForm


class PatientsPageView(TemplateView):
    template_name = 'patients/patients.html'


class PatientsFormView(FormView):
    template_name = 'patients/patient_form.html'
    form_class = PatientForm
    success_url = '/'
