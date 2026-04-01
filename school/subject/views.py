from django.shortcuts import render, redirect
from .models import Subject
from departement.models import Departement
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

def is_teacher(user):
    return user.is_teacher
def is_student(user):
    return user.is_student
def is_admin(user):
    return user.is_admin

# Create your views here.

@login_required
@user_passes_test(is_admin)
def add_subject(request):
    if request.method == 'POST' :
        name = request.POST.get('name') 
        code = request.POST.get('code') 
        description = request.POST.get('description') 
        
        departement_id = request.POST.get('departement_id')
        departement = Departement.objects.get(id = departement_id)
        
        
        Subject.objects.create( 
            name=name, 
            code=code, 
            description=description,
            departement=departement,  
        )
        messages.success(request, 'Subject added Successfully') 
        return redirect('add_subject') 
    else :
        departements_list = Departement.objects.all()
        context = {'departements_list' : departements_list}
        return render(request, 'subject/add-subject.html', context)

@login_required
def subject_list(request):
    subjects_list = Subject.objects.all()
    context = {'subjects_list' : subjects_list}
    return render(request, 'subject/subjects.html', context)

@login_required
@user_passes_test(is_teacher)
def edit_subject(request, subject_id): 
    subject = Subject.objects.get(id = subject_id)
    departements_list = Departement.objects.all()
    context = {
        'subject' : subject,
        'departements_list' : departements_list,
    }

    if request.method == 'POST': 
        subject.name = request.POST.get('name') 
        subject.code = request.POST.get('code') 
        subject.description = request.POST.get('description')
        
        departement_id = request.POST.get('departement_id')
        subject.departement = Departement.objects.get(id = departement_id)

        subject.save()

        messages.success(request, 'Subject edited Successfully') 
        return redirect('subject_list')
    else:
        return render(request, 'subject/edit-subject.html', context)

@login_required
@user_passes_test(is_teacher)  
def delete_subject(request, subject_id):
    subject = Subject.objects.get(id = subject_id)
    if request.method == 'POST':
        subject.delete()
        return redirect('subject_list')
