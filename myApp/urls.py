from django.urls import path
from myApp.views import *

urlpatterns = [
    path('',signupPage,name='signupPage'),
    path('signinPage/',signinPage,name='signinPage'),
    path('logoutPage/',logoutPage,name='logoutPage'),
    path('task/', task_list, name='task_list'),
    path('add-task/', add_task, name='add_task'),
    path('update-task/<str:t_id>/', update_task, name='update_task'),
    path('delete-task/<str:t_id>/', delete_task, name='delete_task'),
]
