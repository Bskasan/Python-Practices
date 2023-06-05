
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserView

# Built-in Sign up Function of Django Rest Framework
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('', UserView)

urlpatterns = [
    path('', include(router.urls)),
    path('login', obtain_auth_token)
]



