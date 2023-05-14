
from django.db import models

# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=30)
    special=models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class Patient(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    doctor=models.ManyToManyField(Doctor)


    def __str__(self) -> str:
        return self.name


class Appointment(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date=models.DateField()

    def __str__(self) -> str:
        return f"{self.patient} {self.doctor} {self.date}"


class MedicalRecord(models.Model):
    patient=models.OneToOneField(Patient,on_delete=models.CASCADE,)
    diagnosis=models.TextField(max_length=200)
    treatment=models.TextField(max_length=200)

    def __str__(self) -> str:
        return f"{self.patient} {self.diagnosis}"