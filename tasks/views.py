from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from tasks.models import ContactItem, TaskItem, AssignedContacts
from tasks.serializers import ContactItemSerializer, TaskItemSerializer, UserSerializer, AssignedContactsSerializer
from django.contrib.auth.models import User

class LoginView(ObtainAuthToken):
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
        
        
class AssignedContactsViewSet(viewsets.ModelViewSet):
    queryset = AssignedContacts.objects.all()
    serializer_class = AssignedContactsSerializer        
class TaskItemViewSet(viewsets.ModelViewSet):
    queryset = TaskItem.objects.all()
    serializer_class = TaskItemSerializer
        
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
        
class ContactsViewSet(viewsets.ModelViewSet):
    queryset = ContactItem.objects.all()
    serializer_class = ContactItemSerializer

