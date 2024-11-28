# tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('get_started/', views.get_started, name='get_started'),
    path('about/', views.about, name='about'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/add/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),

    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/edit/', views.task_update, name='task_update'),
    path('tasks/<int:pk>/update-status/', views.task_update_status, name='task_update_status'),
]
