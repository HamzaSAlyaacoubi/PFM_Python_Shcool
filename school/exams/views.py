from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Exam, ExamResult
from student.models import Student
from teacher.models import Teacher
from subject.models import Subject
from departement.models import Departement

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
    subjects_list = request.user.teacher.subjects.all()
    context = {
        'teachers' : teachers,
        'subjects_list': subjects_list
    }
    

    if request.method == 'POST':
        teacher_id = request.POST['teacher_id']
        teacher = Teacher.objects.get(id = teacher_id)
        
        departement_id = request.POST['departement_id']
        departement = Departement.objects.get(id = departement_id)
        
        subject_id = request.POST['subject_id']
        subject = Subject.objects.get(id = subject_id)
        
        Exam.objects.create(
            name=request.POST['name'],
            subject=subject,
            exam_date=request.POST['exam_date'],
            start_time=request.POST['start_time'],
            end_time=request.POST['end_time'],
            teacher=teacher,
            departement=departement,
        )
        messages.success(request, "Exam added successfully")
        return redirect('exam_list')

    return render(request, 'exams/exam_add.html', context)

@login_required
@user_passes_test(is_admin_or_teacher)
def edit_exam(request, id):
    exam = get_object_or_404(Exam, id = id)
    teachers = Teacher.objects.all()
    subjects_list = request.user.teacher.subjects.all()
    context = {
        'teachers' : teachers,
        'subjects_list': subjects_list,
        'exam' : exam
    }
    

    if request.method == 'POST':
        teacher_id = request.POST['teacher_id']
        teacher = Teacher.objects.get(id = teacher_id)
        
        departement_id = request.POST['departement_id']
        departement = Departement.objects.get(id = departement_id)
        
        subject_id = request.POST['subject_id']
        subject = Subject.objects.get(id = subject_id)
        
        exam.name = request.POST['name']
        exam.subject = subject
        exam.exam_date = request.POST['exam_date']
        exam.start_time = request.POST['start_time']
        exam.end_time = request.POST['end_time']
        exam.teacher = teacher
        exam.departement = departement
        exam.save()

        messages.success(request, "Exam updated")
        return redirect('exam_list')

    return render(request, 'exams/exam_edit.html', context)

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