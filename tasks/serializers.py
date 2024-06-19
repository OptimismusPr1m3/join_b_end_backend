from django.contrib.auth.models import Group, User
from rest_framework import serializers

from tasks.models import ContactItem, TaskItem


class ContactItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactItem
        fields = '__all__'

class TaskItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaskItem
        fields = '__all__'
    

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'last_name', 'first_name']
   
    
class EmailAuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise serializers.ValidationError("Invalid email or password.")

            if not user.check_password(password):
                raise serializers.ValidationError("Invalid email or password.")

            data['user'] = user
            return data
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'.")