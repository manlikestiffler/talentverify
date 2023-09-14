from django.forms import ModelForm
from .models import *
from django import forms


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        
class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        
        
class UpdateEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        

        
