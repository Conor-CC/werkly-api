# api/urls.py
from django.urls import path, include

from . import views

urlpatterns = [
    path('to-do/', views.ListTodo.as_view()),
    path('to-do/<int:pk>/', views.DetailTodo.as_view()),
    path('to-do/<slug:title>/', views.DetailTodo.as_view()),
]
