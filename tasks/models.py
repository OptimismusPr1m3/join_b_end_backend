import datetime
from django.conf import settings
from django.db import models


class TaskItem(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    assignedContacts = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    priority = models.CharField(max_length=15)
    category = models.CharField(max_length=20)
    subtasks = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    uniqueIndex = models.DecimalField(max_digits=50, decimal_places=50)
