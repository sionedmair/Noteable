from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
from django.core import serializers
from .models import Calculator
import os, re, math
import json
from django import forms
from .forms import MyCalculator
from decimal import *

def formview(request):
    '''A view for the main form in which the user must enter certain values'''
    # If the form has been submitted
    if request.method == 'POST':
        form = MyCalculator(request.POST)
        # All validation rules pass
        if form.is_valid():
            # Defining cd and myform
            cd = form.cleaned_data
            myform = MyCalculator()
            i1 = cd['parents']
            i2 = cd['jobs']
            i3 = cd['grants_bursaries_scholarships']
            i4 = cd['student_loan']
            i5 = cd['other_income']
            o1 = cd['rent']
            o2 = cd['travel']
            o3 = cd['bills']
            o4 = cd['other_outcome']
            # Calculating the total income
            totali=i1 + i2 + i3 + i4 + i5
            # Calculating the total outcome
            totalo=o1+o2+o3+o4
            # Calculaint the total variable outcomes
            variable=(totali-totalo)/100
            # Caclulating the recommended spending amount on food
            food= Decimal("43.66")*variable
            # Caclulating the recommended spending amount on socialing
            socialising= Decimal('33.8')*variable
            # Caclulating the amount of money leftover
            leftover = totali - totalo - food - socialising
            # render out.html, a page giving the Calculator's Reslults
            return render(request, 'Noteable_Budgeting/out.html', {'food': food, 'socialising': socialising, 'leftover': leftover})

        # If the form is not valid, display the errors
        else:
            print (form.is_valid())
            print (form.errors)
    # An unbound form - no data to validate
    else:
        form = MyCalculator()
    # pass variables: form
    return render(request, 'Noteable_Budgeting/calculator_list.html', {'form':form})
