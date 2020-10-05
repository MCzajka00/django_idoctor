from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    date_of_birth = models.DateField(null=True)
    personal_identity_number = models.IntegerField(unique=True)
    sex = models.CharField(choices=['male', 'female'])
    # TODO address
    # TODO disease
