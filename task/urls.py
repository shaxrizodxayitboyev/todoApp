from django.urls import path
from task import views

urlpatterns = [
    path('', views.to_do, name='index'),
    path('tasks/', views.to_do_get, name='tasks'),  # For dynamic fetching of tasks
    path('task-receiver/', views.receiver_reminder, name="task-receiver"),  # For marking tasks as done/undone
    path('task/create/', views.create, name='task-create'),  # Task for creating
    path('task/delete/', views.delete_task, name='task-delete'),  # Task for deleting
]