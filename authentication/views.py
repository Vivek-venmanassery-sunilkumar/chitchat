from rest_framework.views import APIView
from .serializers import SignupSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.middleware import csrf
# Create your views here.


class Signup(APIView):  
    def post(self, request):
        data = request.data
        serializer = SignupSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
        
            return Response({'success': True}, status=status.HTTP_201_CREATED)
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        user = authenticate(request, username = username, password = password)    
        if user is None:
            return Response({'message': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)
        
        response = Response({'detail': 'Logged in successfully'}, status=status.HTTP_200_OK)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        response.set_cookie(
            key='access_token',
            value=access_token,
            httponly=True,
            secure=True,
            samesite='Lax'
        )
        
        response.set_cookie(
            key='refresh_token',
            value=refresh_token,
            httponly=True,
            samesite='Lax'
        )

        csrf_token = csrf.get_token(request)
        response.set_cookie(
            key = 'csrftoken',
            value=csrf_token,
            httponly=False,
            secure=True,
            samesite='Lax'
        )

        return response
        

        
        

