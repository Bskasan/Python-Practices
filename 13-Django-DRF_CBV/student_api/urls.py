from django.urls import path

from .views import (
    StudentListCreate
)

# as_view() func -> Class -> Func.
urlpatterns = [
    path('student_list', StudentListCreate.as_view()),
]
