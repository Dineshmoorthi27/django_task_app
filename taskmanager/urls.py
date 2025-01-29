from django.urls import path
from taskmanager import views

urlpatterns=[
    path('',views.task_list,name='task_list'),
    path('edit_task/<int:id>/',views.edit_task,name='edit_task'),
    path('delete_task/<int:id>/',views.delete_Task,name='delete_task'),
    path('task_description/<int:id>',views.task_description,name='task_description')
]