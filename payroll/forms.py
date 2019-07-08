from django import forms
from .models import *

class MonthForm(forms.ModelForm):
    class Meta:
        model = PayslipMonth
        fields = [
            "payslip_month",  
        ]


class EmployeeDetailForm(forms.ModelForm):
    class Meta:
        model = EmployeeDetail
        fields = '__all__'

class UpdateEmployeeDetailForm(forms.ModelForm):
    class Meta:
        model = EmployeeDetail
        fields = '__all__'