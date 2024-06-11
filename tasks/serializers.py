from django.contrib.auth.models import Group, User
from rest_framework import serializers

from tasks.models import ContactItem, TaskItem, AssignedContacts

class AssignedContactsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AssignedContacts
        fields = '__all__'

class ContactItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactItem
        fields = '__all__'

class TaskItemSerializer(serializers.HyperlinkedModelSerializer):
    assignedContacts = AssignedContactsSerializer(many=True)
    class Meta:
        model = TaskItem
        fields = '__all__'
    


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']