from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('all_tasks/', views.all_tasks, name='all_tasks'),
    path('<int:task_id>/', views.task, name='task'),
    path('create_task/', views.create_task, name='create_task'),
    path('<int:task_id>/delete', views.delete_task, name='delete_task'),
]