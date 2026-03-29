from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required, user_passes_test

def is_teacher(user):
    return user.is_teacher
def is_student(user):
    return user.is_student
def is_admin(user):
    return user.is_admin




def index(request):
    return render(request,'authentication/login.html')

@login_required
@user_passes_test(is_student)
def dashboard(request): 
    return render(request, 'students/student-dashboard.html')

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request): 
    return render(request, 'Home/index.html')

@login_required
@user_passes_test(is_teacher)
def teacher_dashboard(request):
    return render(request, 'teachers/teacher-dashboard.html')
