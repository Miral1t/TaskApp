from django.shortcuts import render
from .models import Task
class TaskListView(ListView):  # type: ignore
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'task'

