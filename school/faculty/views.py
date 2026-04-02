from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required, user_passes_test
from student.models import Student
from departement.models import Departement

def is_teacher(user):
    return user.is_teacher
def is_student(user):
    return user.is_student
def is_admin(user):
    return user.is_admin




def index(request):
    return render(request,'authentication/login.html')

@login_required
def dashboard(request): 
    if request.user.is_student :
        return redirect('student_dashboard')
    if request.user.is_teacher :
        return redirect('teacher_dashboard')
    if request.user.is_admin :
        return redirect('admin_dashboard')

@login_required
@user_passes_test(is_student)
def student_dashboard(request): 
    return render(request, 'students/student-dashboard.html')

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request): 
    students_number = Student.objects.all().count()
    departements_number = Departement.objects.all().count()
    context = {
        'students_number' : students_number,
        'departements_number' : departements_number
    }
    return render(request, 'Home/index.html', context)

@login_required
@user_passes_test(is_teacher)
def teacher_dashboard(request):
    return render(request, 'teachers/teacher-dashboard.html')
