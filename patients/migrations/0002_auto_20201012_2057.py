# Generated by Django 3.1.1 on 2020-10-12 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.CharField(choices=[('0', 'male'), ('1', 'female')], max_length=20),
        ),
    ]
