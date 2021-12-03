from django.db import reset_queries
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.utils import timezone

from .models import Task

# Create your views here.
def index(request):
    return HttpResponse("Welcome to my Project")

def all_tasks(request):
    '''
    Return a dictionary with all tasks
    '''
    if request.method == 'GET':
        tasks_title = Task.objects.all()
        return render(request, 'polls/all_tasks.html', {'tasks_title': tasks_title})

def task(request, task_id):
    '''
    Return an specific task by its title
    '''
    if request.method == 'GET':
        task = get_object_or_404(Task, pk = task_id)
        return render(request, 'polls/task.html', {'task': task})

def create_task(request):
    '''
    Create a task
    '''
    if request.method == 'POST':
        task = Task.objects.create(title=request.POST['title'], pub_date=timezone.now(), description=request.POST['description'])
        return render(request, 'polls/task.html', {'task': task})

def delete_task(request, task_id):
    '''
    Delete a task
    '''
    if request.method == 'POST':
        print()
        task = get_object_or_404(Task, pk = request.POST['task_id'])
        task.delete()

        tasks_title = Task.objects.all()
        return render(request, 'polls/all_tasks.html', {'tasks_title': tasks_title})