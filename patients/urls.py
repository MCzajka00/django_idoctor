from xml.etree.ElementInclude import include

from django.urls import path

from patients.views import PatientsPageView, PatientsFormView

urlpatterns = [
    path('', PatientsPageView.as_view(), name='patients'),
    path('add/', PatientsFormView.as_view(), name='patients_form')

]
