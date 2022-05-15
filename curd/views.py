from django.shortcuts import render
from .forms import StudentRegistration
from .models import Student
# Create your views here.

def index(request):
    data = Student.objects.all()
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            address = fm.cleaned_data['address']
            phone = fm.cleaned_data['phone']
            reg = Student(name=name, email=email, address=address, phone=phone)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    return render(request, 'index.html', {'form': fm, 'data': data})


def update(request,id):
    return render(request,'update.html')


def delete(request,id):
    delt = Student(id = id)
    delt.delete()
  
    
