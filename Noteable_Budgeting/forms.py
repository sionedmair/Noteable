from django import forms

class MyCalculator(forms.Form):
    '''A class for a form with all the user's incomes and fixed outcomes'''
    parents = forms.DecimalField(required=True)
    jobs = forms.DecimalField(required=True)
    grants_bursaries_scholarships = forms.DecimalField(required=True)
    student_loan = forms.DecimalField(required=True)
    other_income = forms.DecimalField(required=True)
    rent = forms.DecimalField(required=True)
    travel = forms.DecimalField(required=True)
    bills = forms.DecimalField(required=True)
    other_outcome = forms.DecimalField(required=True)
