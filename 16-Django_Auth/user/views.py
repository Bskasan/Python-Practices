from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import RegistrationSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            return Response({'message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        user = serializer.save()
        token = Token.objects.create(
            user=user
        )

        # Adding token to serializer data to be seen on Front-end
        data = serializer.data
        data['token'] = token.key

        headers = self.get_success_headers(serializer.data)
        return Response({'message':'User created successfully!'}, status.HTTP_201_CREATED, headers=headers)
        
        return super().create(request, *args, **kwargs)