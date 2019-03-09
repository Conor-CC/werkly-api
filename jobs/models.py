from django.db import models
from django.db import models
from django.core.validators import RegexValidator

class Job(models.Model):
    name = models.CharField(max_length=100)
    
