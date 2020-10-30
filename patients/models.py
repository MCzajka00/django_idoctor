from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    date_of_birth = models.DateField(null=True)
    personal_identity_number = models.IntegerField(unique=True)
    sex = models.CharField(choices=[('0', 'male'), ('1', 'female')], max_length=20)

    # TODO address
    # TODO disease

    def __str__(self):
        return f"{self.first_name} {self.last_name}. identity number: {self.personal_identity_number}"


class PatientEmail(models.Model):
    email = models.EmailField(max_length=100)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.patient_id.first_name} {self.patient_id.last_name} email: {self.email}"

