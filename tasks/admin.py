from django.contrib import admin

from tasks.models import TaskItem, ContactItem

admin.site.register(TaskItem)
admin.site.register(ContactItem)
