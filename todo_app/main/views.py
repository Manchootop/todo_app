from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from todo_app.main.models import Task


class ListTasksView(views.ListView):
    template_name = 'tasks_list.html'
    model = Task
    context_object_name = 'tasks'


class ShowTaskDetailsView(views.DetailView):
    template_name = 'task_details.html'
    model = Task
    context_object_name = 'task'


class CreateTaskView(views.CreateView):
    template_name = 'task_create.html'
    model = Task
    fields = '__all__'

    success_url = reverse_lazy('tasks')
