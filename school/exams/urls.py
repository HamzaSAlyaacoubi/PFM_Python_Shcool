from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam_list, name='exam_list'),
    path('finished', views.exam_finished_list, name='exam_finished_list'),
    path('add/', views.add_exam, name='add_exam'),
    path('edit/<str:id>/', views.edit_exam, name='edit_exam'),
    path('delete/<str:id>/', views.delete_exam, name='delete_exam'),
    path('result/add/<str:exam_id>/', views.add_result, name='add_result'),
    path('finished/<str:exam_id>/', views.finish_exam, name='finish_exam'),
    path('notFinished/<str:exam_id>/', views.not_finish_exam, name='not_finish_exam'),
    path('<str:exam_id>/results', views.exam_results, name='exam_results'),
    
]