from django.urls import path

from .views import (
    StudentListCreate,
    StudentDetailUpdateDelete,
)

# as_view() func -> Class -> Func.
urlpatterns = [
    path('student_list_create/', StudentListCreate.as_view()),
    path('student_detail_update_delete/<int:pk>', StudentDetailUpdateDelete.as_view()),
]
