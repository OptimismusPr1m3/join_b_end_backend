import datetime
from django.conf import settings
from django.db import models

    
class TaskItem(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    assignedContacts = models.JSONField(default=None)
    date = models.DateField(default=datetime.date.today)
    priority = models.CharField(max_length=15)
    category = models.CharField(max_length=20)
    subtasks = models.JSONField(max_length=50, default=None)
    state = models.CharField(max_length=20)
    uniqueIndex = models.CharField(max_length=50)

class ContactItem(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    mail = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    

