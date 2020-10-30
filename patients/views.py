from urllib import request

from django.db.models import F
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, FormView

from patients.forms import PatientForm, PatientEmailForm
from patients.models import Patient, PatientEmail


class PatientsPageView(View):
    def get(self, request):
        # data = Patient.objects.select_related().all()
        data = PatientEmail.objects.all().prefetch_related('patient_id')
        data = Patient.objects.annotate(email=F('patientemail__email')).values('pk', 'first_name', 'last_name',
                                                                               'date_of_birth',
                                                                               'personal_identity_number', 'sex',
                                                                               'email')
        print(20 * '*')
        return render(request, "patients/patients.html", {"data": data})
    # template_name = 'patients/patients.html'


class PatientsFormView(FormView):
    template_name = 'patients/patient_form.html'
    form_class = PatientForm
    success_url = '/patients/add_email'

    def form_valid(self, form):
        patient = form.save()
        self.request.session['patient'] = patient.pk
        return super().form_valid(form)


class PatientsEmailFormView(FormView):
    template_name = 'patients/patient_email_form.html'
    form_class = PatientEmailForm
    success_url = '/patients'

    def form_valid(self, form):
        patient = self.request.session.get("patient")
        obj = Patient.objects.get(id=patient)
        # print('*' * 50)
        # print(patient)
        # print('*' * 50)
        # x = patient.save(commit=False)
        y = form.save(commit=False)
        y.patient_id = obj
        # patient.save()
        y.save()

        return super().form_valid(form)


class PatientEditFormView(View):
    form_class = PatientForm
    template_name = 'patients/patient_form.html'

    def get(self, request, id):
        data = Patient.objects.get(pk=id)
        form = self.form_class(instance=data)
        form.fields['personal_identity_number'].disabled = True

        return render(request, self.template_name, {"form": form})

    def post(self, request, id):
        form = self.form_class(request.POST)
        data = Patient.objects.filter(pk=id).update(
            first_name=form.data.get('first_name'),
            last_name=form.data.get('last_name'),
            date_of_birth=form.data.get('date_of_birth'),
            sex=form.data.get('sex')
        )

        # if form.is_valid():
        return redirect('/patients')

        # return render(request, self.template_name, {'form': form})


class PatientDeleteView(View):
    def get(self, request, id):

        data = Patient.objects.filter(pk=id).delete()

        return redirect('patients')






    # def patient_form_view(request):
#     if request.method == "POST":
#         pf = PatientForm(request.POST)
#         pef = PatientEmailForm(request.POST)
#
#         if pf.is_valid() and pef.is_valid():
#             x = pf.save(commit=False)
#             y = pef.save(commit=False)
#             y.patient_id = x
#             x.save()
#             y.save()
#     else:
#         pf = PatientForm()
#         pef = PatientEmailForm()
#
#     return render(request, 'patients/patient_form.html', {'pef': pef, 'pf': pf})
#
# #  TODO progressive enchancement
