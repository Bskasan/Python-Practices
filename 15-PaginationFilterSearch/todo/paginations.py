from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'numperpage'
    page_query_param = 'pagenum'                   