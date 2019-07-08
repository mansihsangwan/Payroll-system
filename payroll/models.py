from django.db import models
from django.conf import settings
from django.urls import reverse
from datetime import datetime

class PayslipMonth(models.Model):
    payslip_month = models.CharField(max_length = 100, unique = True)

    def __str__(self):
        return str(self.payslip_month)


class EmployeeDetail(models.Model):
    payslip_month = models.ForeignKey(PayslipMonth, on_delete = models.CASCADE)
    employee_id = models.IntegerField()
    employee_name = models.CharField(max_length = 100)
    designation = models.CharField(max_length = 100)
    date_of_joining = models.CharField(max_length = 100)
    pay_period = models.CharField(max_length = 100)
    pay_date = models.CharField(max_length = 100)
    pan_number = models.CharField(max_length = 100)
    basic_salary = models.IntegerField()
    performance_allowance = models.IntegerField()
    bonus_allowance = models.IntegerField()
    account_number = models.IntegerField()
    ifsc_code = models.CharField(max_length = 100)