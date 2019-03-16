from django.db import models
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.postgres.fields import ArrayField
MAX_JOB_SWIPES_ALLOWED = 50

class Tag(models.Model):
	tag = models.CharField(max_length=64, unique=True)

class Details(models.Model):
    job_name = models.CharField(max_length=100)
    date = models.DateField()
    time_from = models.TimeField()
    time_to = models.TimeField()
    duration = models.DurationField()
    pay_per_hour = models.DecimalField(decimal_places=2, max_digits=12)
    tags = models.ManyToManyField(Tag, related_name='job_tags')
    address = models.TextField()
    description = models.TextField()
    required_experience = models.TextField()

class Job(models.Model):
    name = models.CharField(max_length=100)
    employer_id = models.PositiveIntegerField()
    def __str__(self):
        return '%s'%(self.name)
