from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from tasks.models import TaskItem
from tasks.serializers import TaskItemSerializer

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
        
        
class TaskItemView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, req, format=None):
        tasks = TaskItem.objects.all()
        serialized_obj = TaskItemSerializer(tasks, many=True)
        return Response(serialized_obj.data)
    
    # def post(self, req, format=None):
        
        

