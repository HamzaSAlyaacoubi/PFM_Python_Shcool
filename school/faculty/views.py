from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'authentication/login.html')

def dashboard(request): 
    return render(request, 'students/student-dashboard.html')

def admin_dashboard(request): 
    return render(request, 'Home/index.html')