from django.contrib import admin
from .models import Student
# Register your models here.
# username : anil password : anil1234
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','address','phone')

