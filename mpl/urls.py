from django.urls import path, include
from django.contrib import admin
# from . import views
from .views import *

app_name = "mpl"

urlpatterns = [
    path('', home, name = 'home'),
]