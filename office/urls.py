from django.urls import path
from .views import offices_view, office_form, save_office, delete_office

urlpatterns = [
     path('', offices_view, name="offices"),
    path('office_form/', office_form, name="office_form"),
    path('save_office/', save_office, name="save_office"),
    path('delete/office/<int:pk>', delete_office, name="delete_office"),
]