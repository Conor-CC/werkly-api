from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from django.core.exceptions import PermissionDenied

class JobListView(generics.ListAPIView):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = models.Job.objects.all()
    serializer_class = serializers.JobsListSerializer

# Handle all possible worker patch requests to job
class WorkerUpdateView(generics.UpdateAPIView):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = models.Job.objects.all()
    serializer_class = serializers.WorkerUpdateSerializer
    def partial_update(self, serializer_class):
        if self.request.user.user_type == 'W':
            serializer_class.save()
        else:
            PermissionDenied


class CreateJobView(generics.CreateAPIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.JobsCreationSerializer
    queryset = models.Job.objects.all()
    def perform_create(self, serializer_class):
        if self.request.user.user_type == 'E':
            serializer_class.save()
        else:
            PermissionDenied
