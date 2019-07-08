from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.http import Http404,HttpResponseRedirect, \
                        HttpResponse, HttpResponseForbidden
from django.urls import reverse
from .forms import *

def payslip_month(request):

    if request.method == 'POST':
        monthform = MonthForm(request.POST)
        if monthform.is_valid():
            monthform = MonthForm(request.POST)
            new_month = monthform.save()

            return HttpResponseRedirect(reverse('payroll:employee_detail',args=(new_month.id,)))

    monthform = MonthForm()

    context = {
        "monthform":monthform,
    }
    return render(request, 'payslip_month.html', context)


def employee_detail(request, payslip_month_id):

    payslip_months = PayslipMonth.objects.get(id = payslip_month_id)

    if request.method == 'POST':
        employeeform = EmployeeDetailForm(request.POST, instance=payslip_months)
        if employeeform.is_valid():
            employeeform = EmployeeDetailForm(request.POST)
            new_employee = employeeform.save()

    employeeform = EmployeeDetailForm(instance=payslip_months)

    employees = EmployeeDetail.objects.filter(payslip_month = payslip_months)

    context = {
        "employeeform":employeeform,
        "employees":employees,
    }
    return render(request, 'employee_detail.html', context)


def update_employee_detail(request, employee_id):
    """
    Update Employee
    """
    employee = EmployeeDetail.objects.get(id = employee_id)
    payslip_month_id = employee.payslip_month

    if request.method=='POST':
        form = UpdateEmployeeDetailForm(request.POST,request.FILES, instance=employee)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('payroll:employee_detail',args=(payslip_month_id.id,)))
    form = UpdateEmployeeDetailForm(instance=employee)

    context = {
        "form":form
    }
    return render(request, 'update_employee_detail.html', context)


def delete_employee(request, employee_id):
    """
    Delete Brochure
    """
    employee = EmployeeDetail.objects.get(id = employee_id)
    payslip_month_id = employee.payslip_month
    employee.delete()

    return HttpResponseRedirect(reverse('payroll:employee_detail',args=(payslip_month_id.id,)))


def view_slip(request, employee_id):

    employee = EmployeeDetail.objects.get(id = employee_id)
    payslip_month_id = employee.payslip_month.id

    employee_details = EmployeeDetail.objects.filter(id = employee_id)

    payslip_month = PayslipMonth.objects.filter(id = payslip_month_id)

    for employee_detail in employee_details:
        # print(employee_detail.basic_salary)
        dearness_allowance = employee_detail.basic_salary/100 * 10
        house_rent_allowance = employee_detail.basic_salary/100 * 8
        travelling_allowance = employee_detail.basic_salary/100 * 6
        food_allowance = employee_detail.basic_salary/100 * 5
        total_balance = employee_detail.basic_salary + employee_detail.performance_allowance + employee_detail.bonus_allowance + dearness_allowance + house_rent_allowance + travelling_allowance + food_allowance

    context = {
        "employee_details":employee_details,
        "payslip_month":payslip_month,
        "dearness_allowance":dearness_allowance,
        "house_rent_allowance":house_rent_allowance,
        "travelling_allowance":travelling_allowance,
        "food_allowance":food_allowance,
        "total_balance":total_balance
    }
    return render(request, 'view_slip.html', context)