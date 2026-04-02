from django.contrib import admin
from .models import Exam
from .models import ExamResult

# Register your models here.
@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'exam_date')
