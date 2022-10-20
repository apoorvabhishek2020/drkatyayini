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
    submission_date = models.DateTimeField()
    description = models.TextField()
    medicines = models.ManyToManyField('Medicine', blank = True)
    
class Medicine(models.Model):
    name = models.CharField(max_length=50)
    composition = models.TextField()

    def __str__(self) -> str:
        return self.name