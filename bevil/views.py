from django.shortcuts import render

# bevil/views.py
from django.http import HttpResponse

def hello_bevil(request):
    return HttpResponse("Hello, this is Bevil's custom page!")
