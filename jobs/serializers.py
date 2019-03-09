from rest_framework import serializers
from . import models

class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Job
        fields = ('id', 'name')
