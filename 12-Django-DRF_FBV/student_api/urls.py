from django.urls import path
from .views import (
    home,
    student_list,
    student_create,
)


urlpatterns = [
    path('', home),
    path('student_list/', student_list), # Show All List
    path('student_create', student_create), # New Record
]
