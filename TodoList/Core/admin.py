from django.contrib import admin

# Register your models here.
from .models import todo

admin.site.register(todo)
