from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
# Alternative temporary method
# from rest_framework.pagination import PageNumberPagination

from .paginations import CustomPageNumberPagination

from .serializers import Todo, TodoSerializer


# Create your views here.
class TodoView(ModelViewSet):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = CustomPageNumberPagination # Local Setting for Todo View.
    

    # Alternative temporary method
    # PageNumberPagination.page_size = 25
    # PageNumberPagination.page_size_query_param = 'numperpage'
    # PageNumberPagination.page_query_param = 'pagenum'