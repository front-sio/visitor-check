from django.urls import path
from webapp.views import *

urlpatterns = [
    path('', home, name="home"),
]