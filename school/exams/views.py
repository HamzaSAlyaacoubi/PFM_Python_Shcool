from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Exam, ExamResult
from student.models import Student
from teacher.models import Teacher

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
def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'exams/exam_list.html', {'exams': exams})

@login_required
@user_passes_test(is_admin_or_teacher)
def add_exam(request):
    teachers = Teacher.objects.all()

    if request.method == 'POST':
        Exam.objects.create(
            name=request.POST['name'],
            subject=request.POST['subject'],
            exam_date=request.POST['exam_date'],
            start_time=request.POST['start_time'],
            end_time=request.POST['end_time'],
            teacher_id=request.POST['teacher']
        )
        messages.success(request, "Exam added successfully")
        return redirect('exam_list')

    return render(request, 'exams/exam_add.html', {'teachers': teachers})

@login_required
@user_passes_test(is_admin_or_teacher)
def edit_exam(request, id):
    exam = get_object_or_404(Exam, id=id)
    teachers = Teacher.objects.all()

    if request.method == 'POST':
        exam.name = request.POST['name']
        exam.subject = request.POST['subject']
        exam.exam_date = request.POST['exam_date']
        exam.start_time = request.POST['start_time']
        exam.end_time = request.POST['end_time']
        exam.teacher_id = request.POST['teacher']
        exam.save()

        messages.success(request, "Exam updated")
        return redirect('exam_list')

    return render(request, 'exams/exam_edit.html', {'exam': exam, 'teachers': teachers})

@login_required
@user_passes_test(is_admin_or_teacher)
def delete_exam(request, id):
    exam = get_object_or_404(Exam, id=id)
    exam.delete()
    messages.success(request, "Exam deleted")
    return redirect('exam_list')

@login_required
@user_passes_test(is_admin_or_teacher)
def add_result(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    students = Student.objects.all()

    if request.method == 'POST':
        ExamResult.objects.create(
            exam=exam,
            student_id=request.POST['student'],
            mark=request.POST['mark'],
            status=request.POST['status']
        )
        messages.success(request, "Result saved")
        return redirect('exam_list')

    return render(request, 'exams/result_add.html', {'exam': exam, 'students': students})