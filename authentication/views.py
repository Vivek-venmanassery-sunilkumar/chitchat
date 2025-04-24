from rest_framework.views import APIView
from .serializers import SignupSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import CustomUser
# Create your views here.


class Signup(APIView):  
    def post(self, request):
        data = request.data
        serializer = SignupSerializer(data)
        if serializer.is_valid():
            serializer.save()
        
            return Response({'success': True}, status=status.HTTP_201_CREATED)
        return Response({serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self, request):
        data = request.data

        email = data['email']
        password = data['password']
        user = authenticate(request, email, password)
        if user is not None:
            return Response({'success': True}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)
        
