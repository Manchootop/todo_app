from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import views as views
from . import views

urlpatterns = [
    path('tasks/', views.ListTasksView.as_view(), name='tasks'),
    path('tasks/<int:pk>/', views.ShowTaskDetailsView.as_view(), name='task-details'),
    path('tasks-create', views.CreateTaskView.as_view(), name='task-create'),
    path('tasks-edit/<int:pk>', views.EditTaskView.as_view(), name='task-edit'),
    path('tasks-delete/<int:pk>', views.DeleteTaskView.as_view(), name='task-delete'),

    path('logout/', LogoutView.as_view(next_page='login'), name='logout')
    path('login/', views.LoginView.as_view(), name='login')
]
