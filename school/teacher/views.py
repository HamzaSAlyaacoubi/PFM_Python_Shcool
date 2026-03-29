from django.shortcuts import render, redirect
from .models import Teacher
from departement.models import Departement
from django.contrib import messages


# Create your views here.
def teacher_dashboard(request):
    return render(request, 'teachers/teacher-dashboard.html')

def add_teacher(request):
    if request.method == 'POST' :
        first_name = request.POST.get('first_name') 
        last_name = request.POST.get('last_name') 
        teacher_id = request.POST.get('teacher_id') 
        gender = request.POST.get('gender') 
        date_of_birth = request.POST.get('date_of_birth') 
        joining_date = request.POST.get('joining_date') 
        mobile_number = request.POST.get('mobile_number') 
        teacher_image = request.FILES.get('teacher_image')
        
        departement_id = request.POST.get('departement_id')
        departement = Departement.objects.get(id = departement_id)
        
        Teacher.objects.create( 
            first_name=first_name, 
            last_name=last_name, 
            teacher_id=teacher_id, 
            gender=gender, 
            date_of_birth=date_of_birth, 
            joining_date=joining_date, 
            mobile_number=mobile_number,
            departement= departement, 
            teacher_image=teacher_image, 
        )
        messages.success(request, 'Teacher added Successfully') 
        return redirect('add_teacher') 
    else :
        departements_list = Departement.objects.all()
        context = {'departements_list': departements_list}
        return render(request, 'teachers/add-teacher.html', context)

def teacher_list(request):
    teacher_list = Teacher.objects.all()
    context = {'teacher_list' : teacher_list}
    return render(request, 'teachers/teachers.html', context)

def view_teacher(request, teacher_id):
    teacher = Teacher.objects.get(teacher_id = teacher_id)
    context = {'teacher': teacher}
    return render(request, 'teachers/teacher-details.html', context)

def edit_teacher(request, teacher_id): 
    teacher = Teacher.objects.get(teacher_id = teacher_id)
    departements_list = Departement.objects.all()
    context = {'departements_list': departements_list, 'teacher' : teacher}

    if request.method == 'POST': 
        teacher.first_name = request.POST.get('first_name') 
        teacher.last_name = request.POST.get('last_name') 
        teacher.teacher_id = request.POST.get('teacher_id') 
        teacher.gender = request.POST.get('gender') 
        teacher.date_of_birth = request.POST.get('date_of_birth') 
        teacher.joining_date = request.POST.get('joining_date') 
        teacher.mobile_number = request.POST.get('mobile_number') 
        teacher.teacher_image = request.FILES.get('teacher_image') 
        
        departement_id = request.POST.get('departement_id')
        teacher.departement = Departement.objects.get(id = departement_id)

        if request.FILES.get('teacher_image'):
            teacher.teacher_image = request.FILES.get('teacher_image')

        teacher.save()

        messages.success(request, 'Teacher edited Successfully') 
        return redirect('teacher_list')
    else:
        return render(request, 'teachers/edit-teacher.html', context)
    
def delete_teacher(request, teacher_id):
    teacher = Teacher.objects.get(teacher_id = teacher_id)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
