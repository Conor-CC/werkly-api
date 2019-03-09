from django.db import models
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.postgres.fields import ArrayField
MAX_JOB_SWIPES_ALLOWED = 20


class Job(models.Model):
    name = models.CharField(max_length=100)
