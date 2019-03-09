# api/urls.py
from django.urls import path, include

from . import views

urlpatterns = [
    path('list/', views.JobListView.as_view()),
    path('create/', views.CreateJobView.as_view()),
    path('worker-update/<int:pk>/', views.WorkerUpdateView.as_view()),
]
