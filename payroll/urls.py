from django.urls import path, re_path
from .views import *

app_name= 'payroll'

urlpatterns = [
    path('', payslip_month, name = 'payslip_month'),
    path('emplyee_detail/<int:payslip_month_id>', employee_detail, name = 'employee_detail'),
    path('update_employee_detail/<int:employee_id>', update_employee_detail, name = 'update_employee_detail'),
    path('delete_employee/<int:employee_id>', delete_employee, name = 'delete_employee'),
    path('view_slip/<int:employee_id>', view_slip, name = 'view_slip'),
]