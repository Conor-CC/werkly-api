# users/serializers.py
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'username', 'user_type')
