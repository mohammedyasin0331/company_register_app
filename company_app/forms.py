from django import forms
from .models import Company, Employee
class CompanyForm(forms.ModelForm):
   class Meta:
     model = Company
     fields = '__all__'
class EmployeeForm(forms.ModelForm):
   class Meta:
     model = Employee
     fields = '__all__'
