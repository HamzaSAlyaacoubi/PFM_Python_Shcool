from django.shortcuts import render, redirect 
from django.http import HttpResponse 
from .models import Student, Parent 
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required, user_passes_test

def is_teacher(user):
    return user.is_teacher
def is_student(user):
    return user.is_student
def is_admin(user):
    return user.is_admin
def is_admin_or_teacher(user):
    return user.is_authenticated and (user.is_admin or user.is_teacher)

@login_required
def student_list(request): 
    student_list = Student.objects.all()
    context = {'student_list': student_list}
    return render(request, 'students/students.html', context) 

@login_required
@user_passes_test(is_admin_or_teacher)
def add_student(request): 
    if request.method == 'POST': 
        # Récupérer les données de l'étudiant 
        first_name = request.POST.get('first_name') 
        last_name = request.POST.get('last_name') 
        student_id = request.POST.get('student_id') 
        gender = request.POST.get('gender') 
        date_of_birth = request.POST.get('date_of_birth') 
        student_class = request.POST.get('student_class') 
        joining_date = request.POST.get('joining_date') 
        mobile_number = request.POST.get('mobile_number') 
        admission_number = request.POST.get('admission_number') 
        section = request.POST.get('section') 
        student_image = request.FILES.get('student_image') 
 
        # Récupérer les données du parent 
        father_name = request.POST.get('father_name') 
        father_occupation = request.POST.get('father_occupation') 
        father_mobile = request.POST.get('father_mobile') 
        father_email = request.POST.get('father_email') 
        mother_name = request.POST.get('mother_name') 
        mother_occupation = request.POST.get('mother_occupation') 
        mother_mobile = request.POST.get('mother_mobile') 
        mother_email = request.POST.get('mother_email') 
        present_address = request.POST.get('present_address') 
        permanent_address = request.POST.get('permanent_address') 


        parent = Parent.objects.create(
            father_name=father_name, 
            father_occupation=father_occupation, 
            father_mobile=father_mobile, 
            father_email=father_email, 
            mother_name=mother_name, 
            mother_occupation=mother_occupation, 
            mother_mobile=mother_mobile, 
            mother_email=mother_email, 
            present_address=present_address, 
            permanent_address=permanent_address 
        )

        student = Student.objects.create( 
            first_name=first_name, 
            last_name=last_name, 
            student_id=student_id, 
            gender=gender, 
            date_of_birth=date_of_birth, 
            student_class=student_class, 
            joining_date=joining_date, 
            mobile_number=mobile_number, 
            admission_number=admission_number, 
            section=section, 
            student_image=student_image, 
            parent=parent 
        )

        messages.success(request, 'Student added Successfully') 
        return redirect('student_list')
    
    else: 
        return render(request, 'students/add-student.html')


@login_required
@user_passes_test(is_admin_or_teacher)
def edit_student(request, student_id): 
    student = Student.objects.get(id=student_id)
    parent = student.parent

    if request.method == 'POST': 
        # Récupérer les données de l'étudiant 
        student.first_name = request.POST.get('first_name') 
        student.last_name = request.POST.get('last_name') 
        student.student_id = request.POST.get('student_id') 
        student.gender = request.POST.get('gender') 
        student.date_of_birth = request.POST.get('date_of_birth') 
        student.student_class = request.POST.get('student_class') 
        student.joining_date = request.POST.get('joining_date') 
        student.mobile_number = request.POST.get('mobile_number') 
        student.admission_number = request.POST.get('admission_number') 
        student.section = request.POST.get('section') 
        student.student_image = request.FILES.get('student_image') 
 
        # Récupérer les données du parent 
        parent.father_name = request.POST.get('father_name') 
        parent.father_occupation = request.POST.get('father_occupation') 
        parent.father_mobile = request.POST.get('father_mobile') 
        parent.father_email = request.POST.get('father_email') 
        parent.mother_name = request.POST.get('mother_name') 
        parent.mother_occupation = request.POST.get('mother_occupation') 
        parent.mother_mobile = request.POST.get('mother_mobile') 
        parent.mother_email = request.POST.get('mother_email') 
        parent.present_address = request.POST.get('present_address') 
        parent.permanent_address = request.POST.get('permanent_address') 


        if request.FILES.get('student_image'):
            student.student_image = request.FILES.get('student_image')

        parent.save()
        student.save()


        messages.success(request, 'Student edited Successfully') 
        return redirect('student_list')
    else:
        return render(request, 'students/edit-student.html', {'student': student, 'parent': parent})


@login_required
@user_passes_test(is_admin_or_teacher)
def view_student(request, student_id): 
    student = Student.objects.get(id=student_id)
    return render(request, 'students/student-details.html', {'student': student}) 
 
@login_required
@user_passes_test(is_admin_or_teacher)
def delete_student(request, student_id): 
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')


@login_required
@user_passes_test(is_admin_or_teacher)
def student_profile_view(request):
    user = request.user

    # Security check
    if not user.is_student:
        return HttpResponseForbidden("You are not allowed to view this page")

    return render(request, "students/student-profile.html", {
        "student": user
    })