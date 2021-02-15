from django.db import models

# Create your models here.

class Deadline(models.Model):
    assignment = models.CharField(max_length=200)
    due_date = models.DateTimeField('date published')

