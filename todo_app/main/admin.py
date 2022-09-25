from django.contrib import admin

from todo_app.main.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
