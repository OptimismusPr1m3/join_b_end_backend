import datetime
from django.conf import settings
from django.db import models


class AssignedContacts(models.Model):
    initials = models.CharField(max_length=5)
    color = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.first_name}  {self.last_name}"
    
class TaskItem(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    assignedContacts = models.ManyToManyField(AssignedContacts, default=None)
    date = models.DateField(default=datetime.date.today)
    priority = models.CharField(max_length=15)
    category = models.CharField(max_length=20)
    subtasks = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    uniqueIndex = models.DecimalField(max_digits=50, decimal_places=50)

class ContactItem(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    mail = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    

