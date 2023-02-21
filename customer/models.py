from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    display_name = models.CharField(max_length=200, null=True, blank=True)
    company_or_organization_name = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    ward = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, default="Tanzania", null=True, blank=True)

    def __str__(self):
        return str(self.display_name)



class Receptionist(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    customer = models.OneToOneField(Customer, on_delete=models.DO_NOTHING, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    company_or_organization_name = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    ward = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, default="Tanzania", null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)


class License(models.Model):
    id_number = models.CharField(max_length=50, null=True, blank=True)
    FirstName = models.CharField(null=True, blank=True, max_length=50)
    MiddleName = models.CharField(null=True, blank=True, max_length=50)
    LastName = models.CharField(null=True, blank=True, max_length=50)
    DateofBirth = models.DateField(null=True, blank=True)
    Sex = models.CharField(null=True, blank=True, max_length=50)

    
    def __str__(self):
        return self.FirstName+' '+self.LastName

class Passport(models.Model):
    id_number = models.CharField(max_length=50, null=True, blank=True)
    FirstName = models.CharField(null=True, blank=True, max_length=50)
    MiddleName = models.CharField(null=True, blank=True, max_length=50)
    LastName = models.CharField(null=True, blank=True, max_length=50)
    DateofBirth = models.DateField(null=True, blank=True)
    Sex = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.FirstName+' '+self.LastName