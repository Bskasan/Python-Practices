from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
# Alternative temporary method
# from rest_framework.pagination import PageNumberPagination

from .paginations import (
    CustomPageNumberPagination,
    CustomLimitOffsetPagination,
    CustomCursorPagination
)

from .serializers import Todo, TodoSerializer


# Create your views here.
class TodoView(ModelViewSet):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = CustomPageNumberPagination # Local Pagination Setting.
    
    # Alternative temporary method
    # PageNumberPagination.page_size = 25
    # PageNumberPagination.page_size_query_param = 'numperpage'
    # PageNumberPagination.page_query_param = 'pagenum'

    # Override
    # Manuel Arama Örneği (Override):
    def get_queryset(self):
        # URL'den parametre değerini yakala:
        title = self.request.query_params.get('title')
        if title is None:
        # Arama yapma (parametre yok)
            return super().get_queryset()
        else:
        # Arama yap:
            # queryset içinde ara:
            return self.queryset.filter(title__contains=title)