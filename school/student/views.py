from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def student_list(request):
    return HttpResponse("<h1> Students_list <h1>")

def add_student(request):
    return HttpResponse("<h1> Add Student <h1>")