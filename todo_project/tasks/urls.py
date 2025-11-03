from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='tasks'),
    path('task/<int:id>/', views.task_detail, name='task'),
    path('create/', views.task_create, name='task-create'),
    path('update/<int:id>/', views.task_update, name='task-update'),
    path('delete/<int:id>/', views.task_delete, name='task-delete'),
]
