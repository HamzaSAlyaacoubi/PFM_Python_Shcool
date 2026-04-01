from django.shortcuts import render, redirect
from .models import Teacher
from departement.models import Departement
from home_auth.models import CustomUser
from subject.models import Subject
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

def is_teacher(user):
    return user.is_teacher
def is_student(user):
    return user.is_student
def is_admin(user):
    return user.is_admin
def is_admin_or_teacher(user):
    return user.is_authenticated and (user.is_admin or user.is_teacher)

# Create your views here.
@login_required
def teacher_dashboard(request):
    return render(request, 'teachers/teacher-dashboard.html')

@login_required
@user_passes_test(is_admin)
def add_teacher(request):
    if request.method == 'POST' :
        first_name = request.POST.get('first_name') 
        last_name = request.POST.get('last_name') 
        gender = request.POST.get('gender') 
        date_of_birth = request.POST.get('date_of_birth') 
        joining_date = request.POST.get('joining_date') 
        mobile_number = request.POST.get('mobile_number') 
        teacher_image = request.FILES.get('teacher_image')
        
        departement_id = request.POST.get('departement_id')
        if (departement_id):
            departement = Departement.objects.get(id = departement_id)
        else :
            departement = None
        
        subjects_ids = request.POST.getlist('subject_id')
        subjects = Subject.objects.filter(id__in=subjects_ids)
                
        teacher = Teacher.objects.create( 
            first_name=first_name, 
            last_name=last_name, 
            gender=gender, 
            date_of_birth=date_of_birth, 
            joining_date=joining_date, 
            mobile_number=mobile_number,
            departement= departement, 
            teacher_image=teacher_image, 
        )
        
        CustomUser.objects.create_user(
            username= f"{first_name}.{last_name}@faculty.com".lower(),
            email= f"{first_name}.{last_name}@faculty.com".lower(),
            teacher=teacher,
            first_name= first_name,
            last_name= last_name,
            is_student=False,
            is_teacher=True,
            password='teacher',
        )
        
        teacher.subjects.set(subjects)
        messages.success(request, 'Teacher added Successfully') 
        return redirect('add_teacher') 
    else :
        departements_list = Departement.objects.all()
        subjects_list = Subject.objects.all()
        context = {'departements_list': departements_list,'subjects_list':subjects_list}
        return render(request, 'teachers/add-teacher.html', context)

@login_required
@user_passes_test(is_admin_or_teacher)
def teacher_list(request):
    teacher_list = Teacher.objects.all()
    context = {'teacher_list' : teacher_list}
    return render(request, 'teachers/teachers.html', context)

@login_required
@user_passes_test(is_admin)
def view_teacher(request, teacher_id):
    teacher = Teacher.objects.get(id = teacher_id)
    teacher_subjects = teacher.subjects.all()
    context = {'teacher': teacher, 'teacher_subjects': teacher_subjects}
    return render(request, 'teachers/teacher-details.html', context)

@login_required
@user_passes_test(is_admin)
def edit_teacher(request, teacher_id): 
    teacher = Teacher.objects.get(id = teacher_id)
    departements_list = Departement.objects.all()
    subjects_list = Subject.objects.all()
    context = {'departements_list': departements_list, 'teacher' : teacher, 'subjects_list':subjects_list}

    if request.method == 'POST': 
        teacher.first_name = request.POST.get('first_name') 
        teacher.last_name = request.POST.get('last_name') 
        teacher.gender = request.POST.get('gender') 
        teacher.date_of_birth = request.POST.get('date_of_birth') 
        teacher.joining_date = request.POST.get('joining_date') 
        teacher.mobile_number = request.POST.get('mobile_number') 
        teacher.teacher_image = request.FILES.get('teacher_image') 
        
        departement_id = request.POST.get('departement_id')
        if (departement_id):
            teacher.departement = Departement.objects.get(id = departement_id)
        else : 
            teacher.departement = None
            
        subjects_ids = request.POST.getlist('subject_id')
        subjects = Subject.objects.filter(id__in=subjects_ids)
        teacher.subjects.set(subjects)

        if request.FILES.get('teacher_image'):
            teacher.teacher_image = request.FILES.get('teacher_image')

        teacher.save()

        messages.success(request, 'Teacher edited Successfully') 
        return redirect('teacher_list')
    else:
        return render(request, 'teachers/edit-teacher.html', context)
    

@login_required
@user_passes_test(is_admin)
def delete_teacher(request, teacher_id):
    teacher = Teacher.objects.get(id = teacher_id)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
