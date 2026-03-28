<<<<<<< HEAD
=======

# Create your views here.
>>>>>>> 572dcd3e678f87c8c198a94e935ebf823858346c
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages 
from .models import CustomUser 
 
<<<<<<< HEAD
# Create your views here.
=======
>>>>>>> 572dcd3e678f87c8c198a94e935ebf823858346c
def signup_view(request): 
    if request.method == 'POST': 
        first_name = request.POST['first_name'] 
        last_name = request.POST['last_name'] 
        email = request.POST['email'] 
        password = request.POST['password'] 
        role = request.POST.get('role')  # student, teacher ou admin 
 
        # Créer l'utilisateur 
        user = CustomUser.objects.create_user( 
            username=email, 
            email=email, 
            first_name=first_name, 
            last_name=last_name, 
            password=password, 
        ) 
<<<<<<< HEAD
 
        # Assigner le rôle
=======

>>>>>>> 572dcd3e678f87c8c198a94e935ebf823858346c
        if role == 'student': 
            user.is_student = True 
        elif role == 'teacher': 
            user.is_teacher = True 
        elif role == 'admin': 
            user.is_admin = True 
 
        user.save() 
        login(request, user) 
        messages.success(request, 'Signup successful!') 
        return redirect('index') 
<<<<<<< HEAD
    return render(request, 'authentication/register.html')

=======
    return render(request, 'authentication/register.html') 
>>>>>>> 572dcd3e678f87c8c198a94e935ebf823858346c

def login_view(request): 
    if request.method == 'POST': 
        email = request.POST['email'] 
        password = request.POST['password'] 
 
        user = authenticate(request, username=email, 
                            password=password) 
        if user is not None: 
            login(request, user) 
            messages.success(request, 'Login successful!') 
            # Redirection selon le rôle 
            if user.is_admin: 
                return redirect('admin_dashboard') 
            elif user.is_teacher: 
                return redirect('teacher_dashboard') 
            elif user.is_student:
                 return redirect('dashboard') 
            else: 
                messages.error(request, 'Invalid user role') 
                return redirect('index') 
        else: 
            messages.error(request, 'Invalid credentials') 
    return render(request, 'authentication/login.html')

def logout_view(request): 
    logout(request) 
    messages.success(request, 'You have been logged out.') 
<<<<<<< HEAD
    return redirect('index')
=======
    return redirect('index') 
>>>>>>> 572dcd3e678f87c8c198a94e935ebf823858346c
