# holidays/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Holiday
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

def is_teacher(user):
    return user.is_teacher
def is_student(user):
    return user.is_student
def is_admin(user):
    return user.is_admin

@login_required
def holiday_list(request):
    holidays = Holiday.objects.all()
    return render(request, 'academic_calendar/holiday.html', {'holidays': holidays})

@login_required
@user_passes_test(is_admin)
def add_holiday(request):
    if request.method == 'POST':
        Holiday.objects.create(
            title=request.POST['title'],
            start_date=request.POST['start_date'],
            end_date=request.POST['end_date'],
            is_school_closed=request.POST.get('is_school_closed') == 'on',
            description=request.POST.get('description')
        )
        messages.success(request, "Holiday added successfully")
        return redirect('holiday_list')

    return render(request, 'academic_calendar/add_holiday.html')

@login_required
@user_passes_test(is_admin)
def edit_holiday(request, id):
    holiday = get_object_or_404(Holiday, id=id)

    if request.method == 'POST':
        holiday.name = request.POST['name']
        holiday.start_date = request.POST['start_date']
        holiday.end_date = request.POST['end_date']
        holiday.is_school_closed = request.POST.get('is_school_closed') == 'on'
        holiday.description = request.POST.get('description')
        holiday.save()

        messages.success(request, "Holiday updated successfully")
        return redirect('holiday_list')

    return render(request, 'academic_calendar/edit_holiday.html', {'holiday': holiday})

@login_required
@user_passes_test(is_admin)
def delete_holiday(request, id):
    holiday = get_object_or_404(Holiday, id=id)
    holiday.delete()
    messages.success(request, "Holiday deleted")
    return redirect('holiday_list')