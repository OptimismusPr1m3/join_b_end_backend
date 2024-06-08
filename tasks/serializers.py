from django.contrib.auth.models import Group, User
from rest_framework import serializers

from tasks.models import TaskItem


class TaskItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaskItem
        fields = '__all__'


