from django.shortcuts import render
from .serializer import (User, UserSerializer, )
from rest_framework.viewsets import ModelViewSet

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer