from django.urls import path
from .views import views as views
from . import views

urlpatterns = [
    path('tasks/', views.ListTasksView.as_view(), name='tasks'),
    path('tasks/<int:pk>/', views.ShowTaskDetailsView.as_view(), name='task-details'),
    path('tasks-create', views.CreateTaskView.as_view(), name='task-create'),
]
