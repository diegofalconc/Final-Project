from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('tasks/', views.tasks, name='tasks'),
    path('about/', views.about, name='about'),
    path('taskdetail/<int:id>', views.taskdetail, name='taskdetail'),
    path('newTask/', views.newTask, name='newtask'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]