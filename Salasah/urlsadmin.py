from django.urls import path
from .import viewsadmin

urlpatterns = [
    path('Backend/',viewsadmin.home, name= 'home'),
]