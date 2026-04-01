from django.shortcuts import render, redirect
from .models import Departement
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
@user_passes_test(is_admin)
def add_departement(request):
    if request.method == 'POST' :
        name = request.POST.get('name') 
        code = request.POST.get('code') 
        description = request.POST.get('description') 
        
        Departement.objects.create( 
            name=name, 
            code=code, 
            description=description,  
        )
        messages.success(request, 'Departement added Successfully') 
        return redirect('add_departement') 
    else :
        return render(request, 'departement/add-departement.html')

@login_required
def departement_list(request):
    departements_list = Departement.objects.all()
    context = {'departements_list' : departements_list}
    return render(request, 'departement/departements.html', context)

@login_required
@user_passes_test(is_admin_or_teacher)
def edit_departement(request, departement_id): 
    departement = Departement.objects.get(id = departement_id)

    if request.method == 'POST': 
        departement.name = request.POST.get('name') 
        departement.code = request.POST.get('code') 
        departement.description = request.POST.get('description') 

        departement.save()

        messages.success(request, 'Departement edited Successfully') 
        return redirect('departement_list')
    else:
        return render(request, 'departement/edit-departement.html', {'departement': departement})
    
@login_required
@user_passes_test(is_admin)
def delete_departement(request, departement_id):
    departement = Departement.objects.get(id = departement_id)
    if request.method == 'POST':
        departement.delete()
        return redirect('departement_list')
