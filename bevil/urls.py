# bevil/urls.py
from django.urls import path
from .views import hello_bevil

urlpatterns = [
    path('', hello_bevil, name='hello_bevil'),  # Custom URL for the app
]
