from django.db import models
from customer.models import Customer
# Create your models here.



class Office(models.Model):
    company = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    activity = models.CharField(max_length=200, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return str(self.name)