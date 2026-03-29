from django.shortcuts import render, redirect
from .models import Departement
from django.contrib import messages


# Create your views here.

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

def departement_list(request):
    departement_list = Departement.objects.all()
    context = {'departement_list' : departement_list}
    return render(request, 'departement/departements.html', context)

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
    
def delete_departement(request, departement_id):
    departement = Departement.objects.get(id = departement_id)
    if request.method == 'POST':
        departement.delete()
        return redirect('departement_list')
