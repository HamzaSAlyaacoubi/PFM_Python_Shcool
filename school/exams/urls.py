from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam_list, name='exam_list'),
    path('add/', views.add_exam, name='add_exam'),
    path('edit/<int:id>/', views.edit_exam, name='edit_exam'),
    path('delete/<int:id>/', views.delete_exam, name='delete_exam'),
    path('result/add/<int:exam_id>/', views.add_result, name='add_result'),
]