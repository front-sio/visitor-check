from django.urls import path, include
from .views import *
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', dashboard, name="customer_dashboard"),
    path('visitors/', visitors_view, name="visitors"),
    path('visitors/save/', save_visitor, name="save_visitor"),
    path('visitor_form/', visitor_form, name="visitor_form"),
    path('visitorform/', saveForm, name="saveForm"),
    path('search_result/', search_view, name="search_result"),
    path('check/', kyc, name="check"),
    path('search_office/', search_office_view, name="search_office"),
    path('search_form/<int:pk>', search_form, name="search_form"),

    path('delete/visitor/<int:pk>', delete_visitor, name="delete_visitor"),
 
]
