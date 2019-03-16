from rest_framework import serializers
from . import models

class JobsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Job
        fields = ('id', 'name')

class WorkerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Job
        fields = ('name',)

class JobsCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Job
        fields = ('id', 'name')
