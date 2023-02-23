from django.db import models
from customer.models import Customer
from office.models import Office




class Visitor(models.Model):
    company  = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    id_number = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True)
    date_of_birth = models.CharField(max_length=200, null=True, blank=True)
    visited_from = models.CharField(max_length=200, null=True, blank=True)
    time_in = models.TimeField(auto_now=True, null=True)
    # time_out = models.TimeField(null=True)
    date_visited = models.DateField(auto_now=True, null=True, blank=True)
    office_visited = models.CharField(max_length=200, null=True, blank=True)
    on_behalf = models.CharField(max_length=200, null=True, blank=True)



  
    def __str__(self):
        return self.first_name+' '+self.last_name