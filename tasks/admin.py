from django.contrib import admin

from tasks.models import TaskItem, AssignedContacts, ContactItem

admin.site.register(TaskItem)
admin.site.register(AssignedContacts)
admin.site.register(ContactItem)
