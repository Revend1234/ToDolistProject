from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('gettodos/', views.gettodos, name='todos'),
    path('todosdetails/<int:id>', views.todosdetails, name='todosdetails'),
    path('newtodo/', views.newtodo, name='newtodo'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]