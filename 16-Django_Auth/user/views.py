from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.generics import CreateAPIView
from .serializers import RegistrationSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer