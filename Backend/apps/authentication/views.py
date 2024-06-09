from django.shortcuts import render
from django.contrib.auth import login as django_login
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import UserProfileSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def register(request):
    serializer = UserProfileSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.validated_data['user']
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token":str(token.key)}, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)