from django.contrib import admin

from .models import Customer, Receptionist, License, Passport



admin.site.register(Customer)
admin.site.register(Receptionist)
admin.site.register(License)
admin.site.register(Passport)
