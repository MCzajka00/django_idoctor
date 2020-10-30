from xml.etree.ElementInclude import include

from django.urls import path

from patients.views import PatientsPageView, PatientsFormView, PatientsFormView, PatientsEmailFormView, \
    PatientEditFormView, PatientDeleteView

urlpatterns = [
    path('', PatientsPageView.as_view(), name='patients'),
    path('add/', PatientsFormView.as_view(), name='patients_form'),
    path('add_email/', PatientsEmailFormView.as_view(), name='patients_email_form'),
    path('edit/<int:id>/', PatientEditFormView.as_view(), name='patients_edit_form'),
    path('delete/<int:id>/', PatientDeleteView.as_view(), name='patient_delete')

]
