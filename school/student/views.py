from django.shortcuts import render, redirect 
<<<<<<< HEAD
from .models import Student, Parent 
from django.contrib import messages
 
def student_list(request): 
    context = {
        'student_list': Student.objects.all()
    }
    return render(request, 'students/students.html', context) 
 
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

=======
from django.http import HttpResponse 
from .models import Student, Parent 
from django.contrib import messages

 
def student_list(request): 
    student_list = Student.objects.all()
    context = {'student_list': student_list}
    return render(request, 'students/students.html', context) 
 
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
 
>>>>>>> 572dcd3e678f87c8c198a94e935ebf823858346c
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
<<<<<<< HEAD
        
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
 
def edit_student(request, student_id): 
    if request.method == "POST" :
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
        
        student = Student.objects.get(id = student_id)
        parent = student.parent
        
        student.first_name=first_name
        student.last_name=last_name
        student.student_id=student_id
        student.gender=gender
        student.date_of_birth=date_of_birth
        student.student_class=student_class
        student.joining_date=joining_date
        student.mobile_number=mobile_number
        student.admission_number=admission_number
        student.section=section
        student.student_image=student_image
        
        student.save()
        
        parent.father_name=father_name 
        parent.father_occupation=father_occupation 
        parent.father_mobile=father_mobile 
        parent.father_email=father_email 
        parent.mother_name=mother_name 
        parent.mother_occupation=mother_occupation 
        parent.mother_mobile=mother_mobile 
        parent.mother_email=mother_email 
        parent.present_address=present_address 
        parent.permanent_address=permanent_address
        
        parent.save()
        
        messages.success(request, 'Student edited Successfully')
        return redirect('edit_student', student_id)
        
        
    else :
        context = {
        'student' : Student.objects.get(id = student_id),
        'parent' : Student.objects.get(id = student_id).parent
        }
        return render(request, 'students/edit-student.html', context) 
 
def view_student(request, student_id): 
    context = {
        'student' : Student.objects.get(id = student_id),
        
    }    
    return render(request, 'students/student-details.html', context) 
 
def delete_student(request, student_id): 
    student = Student.objects.get(id = student_id)
    student.delete()
    return redirect('student_list')
 
def student_dashboard(request): 
    return render(request, 'students/student-dashboard.html')
=======


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
 







def view_student(request, student_id): 
    student = Student.objects.get(id=student_id)
    return render(request, 'students/student-details.html', {'student': student}) 
 
def delete_student(request, student_id): 
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
>>>>>>> 572dcd3e678f87c8c198a94e935ebf823858346c
