from django.urls import path
from .views import *
from customer.views import *
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', avocado_dashboard, name="admin_dashboard"),
    path('customers/', avocado_customers, name="admin_customers"),
    path('visitors/', avocado_visitors, name="admin_visitors"),
    path('save_customer/', save_customer, name="save_customer"),
    path('customer_form/', customer_form, name="customer_form"),
    path('offices/', avocado_offices, name="admin_offices"),

    path('customer/delete/<int:pk>', delete_customer, name="delete_customer"),
    path('customer/update/<int:pk>', customerUpdate, name="update_customer"),
]
