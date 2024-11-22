from django.shortcuts import render, redirect, get_object_or_404
from .models import Tasks
from .forms import TaskForm
from django.template.loader import get_template, render_to_string
from django.http import JsonResponse

def welcome(request):
    try:
        get_template('base.html')  # Debug to check if base.html is found
        return render(request, 'welcome.html')
    except Exception as e:
        print(e)
        raise

def load_task_form(request):
    form = TaskForm()  # Instantiate the form
    return render(request, 'task_form.html', {'form': form})

def load_task_list(request):
    tasks = Tasks.objects.all()  # Get all tasks
    task_list_html = render_to_string('task_list.html', {'tasks': tasks})  # Render the task list with the current tasks
    return JsonResponse({'html': task_list_html})
  
def about(request):
    return render(request, 'about.html')

def task_list(request):
    tasks = Tasks.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save()  # Save the new task
            # After saving, load the updated task list
            tasks = Tasks.objects.all()  # Get all tasks (or filter as needed)
            html = render_to_string('task_list.html', {'tasks': tasks})  # Render updated task list
            return JsonResponse({'status': 'success', 'html': html})  # Return HTML to update the task list
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

def get_started(request):
    return render(request, 'get_started.html')
