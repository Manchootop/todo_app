from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from todo_app.main.forms import UserRegisterForm
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


class EditTaskView(views.UpdateView):
    template_name = 'task_edit.html'
    model = Task
    fields = ('title', 'description', 'complete')

    success_url = reverse_lazy('tasks')


class DeleteTaskView(views.DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')


class LoginView(auth_views.LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    success_url = reverse_lazy('tasks')


class RegisterView(views.CreateView, SuccessMessageMixin):
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"


