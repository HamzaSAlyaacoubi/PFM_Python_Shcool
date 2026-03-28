
# Create your views here.

<<<<<<< HEAD
def index(request):
    return render(request,'authentication/login.html')

def dashboard(request): 
    return render(request, 'students/student-dashboard.html')

def admin_dashboard(request): 
    return render(request, 'Home/index.html')
=======
from django.shortcuts import render, redirect 

 
def index(request): 
    return render(request, 'authentication/login.html')


def dashboard(request): 
    return render(request, 'students/student-dashboard.html') 
>>>>>>> 572dcd3e678f87c8c198a94e935ebf823858346c
