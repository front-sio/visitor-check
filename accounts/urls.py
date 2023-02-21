
from django.urls import path
from .views import *
from customer.views import *
from avocado.views import *
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('profile/', avocado_dashboard, name="admin_profile"),
    path('offices/profile/', avocado_dashboard, name="office_profile"),
    path('receptionist/profile/', avocado_dashboard, name="reception_profile"),
    path('customer/profile/', avocado_dashboard, name="customer_profile"),
    path('login/', UserLogin, name="login"),
    path('logout/', logoutUser, name="logout"),
]



