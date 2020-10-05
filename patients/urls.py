
from xml.etree.ElementInclude import include

from django.urls import path

from patients.views import PatientsPageView

urlpatterns = [
    path('', PatientsPageView.as_view(), name='patients')

]
