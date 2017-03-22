from django.db import models
from django.forms import ModelForm


#A model for a calculator
class Calculator(models.Model):
    '''class representing our calculator variables'''
    parents = models.DecimalField(max_digits=10000, decimal_places=2)
    jobs = models.DecimalField(max_digits=10000, decimal_places=2)
    grants_bursaries_scholarships = models.DecimalField(max_digits=10000, decimal_places=2)
    student_loan = models.DecimalField(max_digits=10000, decimal_places=2)
    other_income = models.DecimalField(max_digits=10000, decimal_places=2)
    rent = models.DecimalField(max_digits=10000, decimal_places=2)
    travel = models.DecimalField(max_digits=10000, decimal_places=2)
    bills = models.DecimalField(max_digits=10000, decimal_places=2)
    other_outcome = models.DecimalField(max_digits=10000, decimal_places=2)
