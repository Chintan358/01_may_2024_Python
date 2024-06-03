from django.contrib import admin
from .models import *
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=["name","email","age","phone"]

admin.site.register(Student,StudentAdmin)


