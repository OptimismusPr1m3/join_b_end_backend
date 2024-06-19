from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import viewsets, status
from tasks.models import ContactItem, TaskItem
from tasks.serializers import ContactItemSerializer, EmailAuthTokenSerializer, TaskItemSerializer, UserRegistrationSerializer, UserSerializer
from django.contrib.auth.models import User

class LoginView(ObtainAuthToken):
    
    def post(self, request):
        serializer = EmailAuthTokenSerializer(data=request.data)
        # serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        })
                
class TaskItemViewSet(viewsets.ModelViewSet):
    queryset = TaskItem.objects.all()
    serializer_class = TaskItemSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
        
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(detail=False, methods=['post'], url_path='register')
    def register(self, request):
        if request.method == 'POST':
            serializer = UserRegistrationSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                return Response( {
                    'first_name': user.first_name,
                    'email': user.email,
                    'last_name': user.last_name,
                }, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ContactsViewSet(viewsets.ModelViewSet):
    queryset = ContactItem.objects.all()
    serializer_class = ContactItemSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

