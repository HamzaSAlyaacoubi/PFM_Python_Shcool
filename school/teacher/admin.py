from django.contrib import admin
from .models import Teacher

# Register your models here.
@admin.register(Teacher)
class adminTeacher(admin.ModelAdmin):
    list_display = ('id','teacher_id','first_name', 'last_name', 'departement')