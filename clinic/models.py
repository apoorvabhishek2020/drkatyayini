from random import choices
from secrets import choice
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models
class Patient(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    address = models.CharField(max_length=200)
    date_of_examination = models.DateTimeField()
    presenting_complaint = models.TextField()
    history_of_presenting_complaint = models.TextField()
    past_medical_history = models.TextField()
    drug_history = models.TextField()
    family_history = models.TextField()
    personal_history = models.ManyToManyField('PersonalHistory', blank = True)
    prescribed_medicines = models.ManyToManyField('Medicine', blank = True)
    bp = models.CharField(max_length=20, verbose_name="BP (mm of Hg)")
    pulse_rate = models.CharField(max_length=20, verbose_name="Pulse Rate (BpM)")
    temperature = models.CharField(max_length=20, verbose_name="Temperature (°F)")
    pallor = models.CharField(max_length=20)
    lcterus = models.CharField(max_length=20)
    clubbing = models.CharField(max_length=20)
    cyanosio = models.CharField(max_length=20)
    lumph_adenopathy = models.CharField(max_length=20)
    edenro = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name
    
class Medicine(models.Model):
    name = models.CharField(max_length=50)
    composition = models.TextField()

    def __str__(self) -> str:
        return self.name

class PersonalHistory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name