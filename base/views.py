from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm


def loginPage(request):
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('base:home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('base:home')
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'page':page}
    return render(request, 'login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('base:home')


def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('base:home')
        else:
            messages.error(request, 'An error occurred during registration')


    return render(request, 'login_register.html', {'form': form})

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else''  
    employees = Employee.objects.filter(
        Q(company__company_name__icontains=q) | 
        Q(employee_name__icontains=q) | 
        Q(employee_ID__icontains=q))
    companies = Company.objects.all()
    companies_count = companies.count
    employees_count = employees.count
    context = { 'companies':companies, 'companies_count':companies_count,'employees_count':employees_count,'employees':employees}
    return render(request, 'home.html', context)


def employee_detail(request, slug):
    employee =Employee.objects.get(slug=slug)
    context = {'employee':employee}
    return render(request, "employee_detail.html", context)

@login_required(login_url='base:login')
def addCompany(request):
    form = CompanyForm
    companies = Company.objects.all()
    if request.method == 'POST':
        Company.objects.create(
            company_name=request.POST.get('company_name'),
            contact_person=request.POST.get('contact_person'),
            slug=request.POST.get('slug'),
            contact=request.POST.get('contact'),
            email_address=request.POST.get('email_address'),
            reg_date=request.POST.get('reg_date'),
            reg_number = request.POST.get('reg_number')
        )
        return redirect('base:home')


    context={'form':form, 'companies':companies}
    return render(request, 'add_company.html', context)

@login_required(login_url='base:login')
def addEmployee(request):
    form = EmployeeForm
    companies = Company.objects.all()
    if request.method == 'POST': 
        company_name = request.POST.get('company')
        company,created = Company.objects.get_or_create(company_name=company_name)
        
        
        Employee.objects.create(
            employee_name=request.POST.get('employee_name'),
            company=company,
            slug=request.POST.get('slug'),
            employee_ID=request.POST.get('employee_ID'),
            date_employed=request.POST.get('date_employed'),
            date_left=request.POST.get('date_left'),
            description=request.POST.get('description'),
         )
        
        return redirect('base:home')


    context={'form':form, 'companies':companies}
    return render(request, 'add_employee.html', context)



@login_required(login_url='base:login')
def updateEmployee(request,slug):
    employee = Employee.objects.get(slug=slug)
    companies = Company.objects.all()
    form = UpdateEmployeeForm(instance=employee)
     
    if request.method =='POST':
        if request.method == 'POST':
            employee.employee_name = request.POST.get('employee_name')
            employee.employee_ID = request.POST.get('employee_ID')
            employee.description = request.POST.get('description')
           
        
        employee.save()
        return redirect('base:home')

    context = {'form':form, 'employee':employee, 'companies':companies}
    return render(request, 'employeeupdate_form.html', context)

