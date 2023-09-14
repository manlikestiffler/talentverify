from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Company(models.Model):
    slug = models.SlugField(max_length=255, unique=True, null=True,blank=True)
    company_name = models.CharField(max_length=300)
    reg_number = models.CharField(blank=False, null=False,max_length=60)
    reg_date = models.DateField(auto_now_add=False, auto_now=False,blank=False,null=False)
    address = models.CharField(max_length=300)
    contact_person = models.CharField(max_length=250,blank=True,null=True)
    departments = models.IntegerField(default='0', blank=False, null=False) 
    contact = models.CharField(blank=False, null=False,max_length=60)
    email_address = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Companies'
        ordering = ['-created']
        
        
    def __str__(self):
        return self.company_name
    
    
class Employee(models.Model):
    slug = models.SlugField(max_length=255, unique=True, null=True,blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,null=True,blank=True)
    employee_name = models.CharField(max_length=300)
    employee_ID = models.CharField(blank=False, null=False, max_length=100)
    description = models.TextField(null=True,blank=True)
    date_employed = models.DateField(auto_now_add=False, auto_now=False,blank=False,null=False)
    date_left = models.DateField(auto_now_add=False, auto_now=False,blank=False,null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
            ordering = ['-updated', '-created']
            
    def get_absolute_url(self):
        return reverse('base:employee-detail', args=[self.slug])
    
    def __str__(self):
        return self.name
    
