from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .serializers import Todo, TodoSerializer

# Create your views here.
class TodoView(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer