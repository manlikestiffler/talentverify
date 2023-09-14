from django.contrib import admin
from .models import *


@admin.register(Company)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'slug']
    prepopulated_fields = {'slug': ('company_name',)}

@admin.register(Employee)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['employee_name', 'slug']
    prepopulated_fields = {'slug': ('employee_name',)}