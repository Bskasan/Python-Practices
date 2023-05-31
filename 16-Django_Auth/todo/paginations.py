from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination,
    CursorPagination
)

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'numperpage'
    page_query_param = 'pagenum'   


class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 25 # Limit
    limit_query_param = 'adet'
    offset_query_param = 'baslangic'

class CustomCursorPagination(CursorPagination):
    page_size = 25
    ordering = 'id'
    cursor_query_param = 'imlec'

