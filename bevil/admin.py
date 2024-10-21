# bevil/admin.py
from django.contrib import admin
from .models import ExampleModel  # Replace with actual models when available

@admin.register(ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Customize fields for display in admin
