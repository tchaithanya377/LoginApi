from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializer import register_serializer
from rest_framework.exceptions import AuthenticationFailed
from .models import resister
# Create your views here.

class register(viewsets.ModelViewSet):
    queryset = resister.objects.all()
    serializer_class = register_serializer

class login(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = resister.objects.filter(email = email).first()

        if user is not None:
            raise  AuthenticationFailed('invalid user')
        # if not user.check_password(password):
        #     raise AuthenticationFailed('invalid password')
        return Response({'message':'done'})