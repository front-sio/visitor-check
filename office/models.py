from django.db import models
from customer.models import Customer
from django.contrib.auth.models import User



class Office(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, null=True)
    company = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    activity = models.CharField(max_length=200, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return str(self.name)