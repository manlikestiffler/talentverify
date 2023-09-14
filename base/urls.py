from django.urls import path
from .import views

app_name = 'base'

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('<slug:slug>', views.employee_detail, name="employee-detail"),
    path('add-company/' , views.addCompany, name="add-company"),
    path('add-employee/' , views.addEmployee, name="add-employee"),
    path('<slug:slug>', views.updateEmployee, name="employee-update-detail"),
]