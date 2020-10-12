from datetime import date

from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateInput

from patients.models import Patient


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'date_of_birth': DateInput(attrs={'type': 'date'})
        }

        def clean_date(self):
            d = self.cleaned_data.get('date')
            if d > date.today():
                raise ValidationError("You can`t be born in the future!")
            raise d
