from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages 
from .models import CustomUser
from django.utils import timezone
from django.contrib.auth.hashers import make_password

from .models import CustomUser, PasswordResetRequest
 
# Create your views here.
def signup_view(request): 
    if request.method == 'POST': 
        first_name = request.POST['first_name'] 
        last_name = request.POST['last_name'] 
        email = request.POST['email'] 
        password = request.POST['password'] 
        role = request.POST.get('role')  # student, teacher ou admin 
        code = request.POST.get("signup_code")
 
        # Créer l'utilisateur 
        user = CustomUser.objects.create_user( 
            username=email, 
            email=email, 
            first_name=first_name, 
            last_name=last_name, 
            password=password, 
        ) 
 
        # Assigner le rôle
        SIGNUP_CODES = {
            "TEACH-2026": "teacher",
            "ADMIN-2026": "admin",
        }

    

    
        user.is_student = True  # default
        if code in SIGNUP_CODES:
            role = SIGNUP_CODES[code]

        

        if role == "teacher":
            user.is_teacher = True
            user.is_student = False

        elif role == "admin":
            user.is_admin = True
            user.is_student = False


        user.save() 
        login(request, user) 
        messages.success(request, 'Signup successful!') 
        return redirect('index') 
    return render(request, 'authentication/register.html')


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
    return redirect('index')

def forgot_password_view(request):
    if request.method == "POST":
        email = request.POST.get("email")

        try:
            user = CustomUser.objects.get(email=email)

            # Create password reset request
            reset_request = PasswordResetRequest.objects.create(
                user=user,
                email=email
            )

            # Send reset email
            reset_request.send_reset_email()

        except CustomUser.DoesNotExist:
            # SECURITY: do nothing different
            pass

        # Always show the same message
        messages.success(
            request,
            "If an account with this email exists, a reset link has been sent."
        )
        return redirect("forgot_password")

    return render(request, "authentication/forgot-password.html")

def reset_password_view(request, token):
    try:
        reset_request = PasswordResetRequest.objects.get(token=token)

        # Check if token expired
        if not reset_request.is_valid():
            messages.error(request, "This reset link has expired.")
            return redirect("forgot_password")

        if request.method == "POST":
            new_password = request.POST.get("new_password")
            confirm_password = request.POST.get("confirm_password")

            if new_password != confirm_password:
                messages.error(request, "Passwords do not match.")
                return render(request, "authentication/reset_password.html")

            # Set new password
            user = reset_request.user
            user.password = make_password(new_password)
            user.save()

            # Delete token after successful reset
            reset_request.delete()

            messages.success(request, "Your password has been reset. You can now log in.")
            return redirect("login")

        return render(request, "authentication/reset_password.html")

    except PasswordResetRequest.DoesNotExist:
        messages.error(request, "Invalid password reset link.")
        return redirect("forgot_password")