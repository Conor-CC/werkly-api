# api/urls.py
from django.urls import path, include


urlpatterns = [
    path('to-do/', include('todos.urls')),
    path('users/', include('users.urls')),
]
