from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
# Alternative temporary method
# from rest_framework.pagination import PageNumberPagination

from .paginations import (
    CustomPageNumberPagination,
    CustomLimitOffsetPagination,
    CustomCursorPagination
)

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .serializers import Todo, TodoSerializer


# Create your views here.
class TodoView(ModelViewSet):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = CustomPageNumberPagination # Local Pagination Setting.

    # Filtrelemen modulleri
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Bire bir eslestirme
    filterset_fields = ['is_done', 'priority', 'id'] # for django_filters module.

    # Search: İçinde arama:
    # https://www.django-rest-framework.org/api-guide/filtering/#searchfilter
    search_fields = ['title', 'description']
    # Ordering: Sıralama:
    ordering_fields = ['id', 'title'] # '__all__'

    
    # Alternative temporary method
    # PageNumberPagination.page_size = 25
    # PageNumberPagination.page_size_query_param = 'numperpage'
    # PageNumberPagination.page_query_param = 'pagenum'

    # Override
    # Manuel Arama Örneği (Override):
    # def get_queryset(self):
    #     # URL'den parametre değerini yakala:
    #     title = self.request.query_params.get('title')
    #     if title is None:
    #     # Arama yapma (parametre yok)
    #         return super().get_queryset()
    #     else:
    #     # Arama yap:
    #         # queryset içinde ara:
    #         return self.queryset.filter(title__contains=title)