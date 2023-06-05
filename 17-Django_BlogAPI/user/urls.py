
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserView

# Built-in Sign up Function of Django Rest Framework
from rest_framework.authtoken.views import obtain_auth_token

# logout Function
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response({"message": 'User Logout: Token Deleted!'})


router = DefaultRouter()
router.register('', UserView)

urlpatterns = [
    path('', include(router.urls)),
    path('login', obtain_auth_token),
    path('logout', logout),

]



