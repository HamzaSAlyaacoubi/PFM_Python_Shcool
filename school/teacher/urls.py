from django.urls import path
from . import views

urlpatterns = ([
    path('dashboard', views.teacher_dashboard, name="teacher_dashboard"),
    path('add/', views.add_teacher, name="add_teacher"),
    path('teachers/', views.teacher_list, name="teacher_list"),
    path('teachers/<str:teacher_id>/', views.view_teacher, name="view_teacher"),
    path('edit/<str:teacher_id>/', views.edit_teacher, name="edit_teacher"),
    path('delete/<str:teacher_id>/', views.delete_teacher, name="delete_teacher"),
])